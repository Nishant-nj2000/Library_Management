from flask import Flask, render_template,abort,jsonify,request,redirect,session
from flask import *  
from flaskext.mysql import MySQL
import re
import time
import os
import string
import requests
import json
from datetime import datetime
from datetime import date

app = Flask(__name__,template_folder = 'template')

app.secret_key = "Library Management"

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Abcde@123'
app.config['MYSQL_DATABASE_DB'] = 'library'
mysql = MySQL(app)


#MySQL Query Driver
def mysql_query(sql):
	connection = mysql.connect()
	cursor = connection.cursor()
	if sql.strip().split(' ')[0].lower() == "select" :
		# print(sql)
		cursor.execute(sql)
		# print(cursor._executed)
		
		columns = [column[0] for column in cursor.description]
		results = []
		for row in cursor.fetchall():
			results.append(dict(zip(columns, row)))
		data = results
		cursor.close()
		connection.close()
		return data
	if sql.strip().split(' ')[0].lower() != "select" :
		cursor.execute(sql)
		print(cursor._executed)
		connection.commit()
		cursor.close()
		connection.close()
		return None
# How to use this function
# --> mysql_query("Select * from user_master;")
# --> mysql_query(" select * from user_master where emailid='{}';".format(email))
#################################################################




# @app.route('/temp')
# def temp():
# 	data = requests.get("https://frappe.io/api/method/frappe-library").json()
# 	cursor = connection.cursor()
# 	for a in data:
# 		for i in range(0,20):
# 			sql = "INSERT INTO books(book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,publication_date,publisher,ratings_count,text_reviews_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"	
			
# 			timestring = datetime.strptime(data['message'][i]['publication_date'],'%m/%d/%Y')
			
# 			dt = (data['message'][i]['bookID'],data['message'][i]['title'],data['message'][i]['authors'],data['message'][i]['average_rating'],data['message'][i]['isbn'],data['message'][i]['isbn13'],data['message'][i]['language_code'],data['message'][i]['  num_pages'],timestring,data['message'][i]['publisher'],data['message'][i]['ratings_count'],data['message'][i]['text_reviews_count'])
# 			cursor.execute(sql,dt)
# 	connection.commit()		
# 	return render_template('parent.html')
	
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/manage_books')
def manage_books():
	data = mysql_query("SELECT * from books")
	data1 = mysql_query("SELECT language_code from books")
	return render_template('manage_books.html',data=data,data1=data1)

@app.route('/update_book', methods=['POST'])
def update_book():
	if request.method == 'POST':
		book_id = request.form['book_id']
		title = request.form['title']
		average_rating = request.form['average_rating']
		authors = request.form['authors']
		language_code = request.form['language_code']
		publication_date = request.form['publication_date']
		publisher = request.form['publisher']
		stock = request.form['stock']
		mysql_query("UPDATE books set title = '{}', average_rating = '{}', authors = '{}', language_code = '{}', publication_date = '{}', publisher = '{}', stock = '{}' where book_id = '{}'".format(title,average_rating,authors,language_code,publication_date,publisher,stock,book_id))
		flash("Book Updated Successfuly !",'success')
	data = mysql_query("SELECT * from books")
	return render_template('manage_books.html',data=data)

@app.route('/delete_book')
def delete_book():
	if request.method == 'POST':
		book_id = request.form['book_id']
		mysql_query("DELETE from books where book_id = '{}'".format(book_id))
		flash("Book Deleted Successfuly !",'warning')
	data = mysql_query("SELECT * from books")
	return render_template('manage_books.html',data=data)


@app.route('/manage_members')
def manage_members():
	data = mysql_query("SELECT * from members")
	return render_template('manage_members.html',data=data)

@app.route('/add_member', methods=['POST'])
def add_member(): 
	if request.method == 'POST' and 'm_name' in request.form and 'mobile' in request.form and 'email_id' in request.form and 'address' in request.form :
		m_name = request.form['m_name']
		mobile = request.form['mobile']
		email_id = request.form['email_id']
		m_address = request.form['address']
		
		account = mysql_query("SELECT member_id from members where email_id='{}' OR mobile='{}'".format(email_id,mobile))
		print(account)
		if len(account) == 0:
			mysql_query("INSERT INTO members(m_name,mobile,email_id,m_address) values ('{}', '{}', '{}', '{}')".format(m_name,mobile,email_id,m_address))
			flash("Member Added Successfully !",'info')	
		else:
			flash('Member Already Exists', 'danger')
			data = mysql_query("SELECT * from members")
			return render_template('manage_members.html',data=data)
	elif request.method == 'POST':
		flash('Please fill the form !','error')
	data = mysql_query("SELECT * from members")
	return render_template('manage_members.html',data=data)

@app.route('/update_member',methods=['POST'])
def update_member():
	if request.method == 'POST':
		member_id = request.form['member_id']
		m_name = request.form['m_name']
		mobile = request.form['mobile']
		email_id = request.form['email_id']
		m_address = request.form['address']
		mysql_query("UPDATE members set m_name = '{}', mobile = '{}', email_id = '{}', m_address = '{}' where member_id = '{}'".format(m_name,mobile,email_id,m_address,member_id))
		flash("Member Updated Successfuly !",'success')
	data = mysql_query("SELECT * from members")
	return render_template('manage_members.html',data=data)

@app.route('/delete_member',methods=['POST'])
def delete_member():
	if request.method == 'POST':
		member_id = request.form['member_id']
		mysql_query("DELETE from members where member_id = '{}'".format(member_id))
		flash("Member Deleted Successfuly !",'warning')
	data = mysql_query("SELECT * from members")
	return render_template('manage_members.html',data=data)

@app.route('/issue_books_page_load')
def issue_books_page_load():
	book_id = mysql_query("SELECT book_id from transactions")
	print(book_id)
	member_id = mysql_query("SELECT member_id from transactions")
	print(member_id)
	result = mysql_query("SELECT b.title,m.m_name from books b,member m,transactions t where b.book_id = t.book_id and m.member_id = t.member_id and b.book_id = '{}' and m.member_id = '{}'".format(book_id,member_id))
	print(result)
	data = mysql_query("SELECT book_id,title from books")
	data1 = mysql_query("SELECT member_id,m_name from members")
	data3 = mysql_query("SELECT * from transactions")	
	return render_template('issue_books.html',data=data,data1=data1,data3=data3)

@app.route('/issue_book',methods=['POST'])
def issue_book():
	if request.method == 'POST':
		book_id = request.form['book_id']
		member_id = request.form['member_id']
		issue_date = date.today()
		mysql_query("INSERT into transactions(book_id,member_id,issue_date) values ('{}','{}','{}')".format(book_id,member_id,issue_date))
	return redirect(url_for('issue_books_page_load'))

if __name__ == "__main__":
	app.run(port='8000', debug=True)