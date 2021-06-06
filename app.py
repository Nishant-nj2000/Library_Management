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
import math


app = Flask(__name__,template_folder = 'template')

app.secret_key = "Library Management"

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Abcde@123'
app.config['MYSQL_DATABASE_DB'] = 'library'
mysql = MySQL(app)


#MySQL Query Driver function
def mysql_query(sql):
	connection = mysql.connect()
	cursor = connection.cursor()
	if sql.strip().split(' ')[0].lower() == "select" :
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


	
@app.route('/')
def main():
	return render_template('index.html')

@app.route('/import_book', methods=['POST'])
def import_book():
	if request.method == 'POST':
		no_of_records = int(request.form['no_of_records'])
		title = request.form['title']
		authors = request.form['authors']
		isbn = request.form['isbn']
		publisher = request.form['publisher']
		list1 = []
		page = no_of_records/20
		rounded_value = math.ceil(page)
		api_data = "https://frappe.io/api/method/frappe-library"
		parameters = {'page':no_of_records,'title':title,'authors':authors,'isbn':isbn,'publisher':publisher}
		connection = mysql.connect()
		cursor = connection.cursor()
		#using loop for inserting n number of records 
		for a in range(0,rounded_value):
			list2 = []
			request_data = requests.get(url=api_data,params=parameters)
			list2 = request_data.json()
			list1.append(list2)
		for a in list1:
			for b in range(0,no_of_records):
				book_id = a['message'][0]['bookID']
				data_check = mysql_query("SELECT book_id from books where book_id = '{}'".format(book_id))
				if len(data_check) == 0:
					sql = "INSERT INTO books(book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,publication_date,publisher,ratings_count,text_reviews_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
					timestring = datetime.strptime(a['message'][b]['publication_date'],'%m/%d/%Y')
					dt = (a['message'][b]['bookID'],a['message'][b]['title'],a['message'][b]['authors'],a['message'][b]['average_rating'],a['message'][b]['isbn'],a['message'][b]['isbn13'],a['message'][b]['language_code'],a['message'][b]['  num_pages'],timestring,a['message'][b]['publisher'],a['message'][b]['ratings_count'],a['message'][b]['text_reviews_count'])
					cursor.execute(sql,dt)
				else:
					mysql_query("UPDATE books set stock = stock + '{}' where book_id = '{}'".format(1,book_id))
			flash("Books Imported Successfully !",'success')
			connection.commit()
		return redirect(url_for('manage_books'))	 


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
		mysql_query("UPDATE books set title = '{}', average_rating = '{}', authors = '{}', language_code = '{}', publication_date = '{}', publisher = '{}' where book_id = '{}'".format(title,average_rating,authors,language_code,publication_date,publisher,book_id))
		flash("Book Updated Successfuly !",'success')
	data = mysql_query("SELECT * from books")
	return render_template('manage_books.html',data=data)

@app.route('/delete_book', methods=['POST'])
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
	data = mysql_query("SELECT book_id,title from books")
	data1 = mysql_query("SELECT member_id,m_name from members")
	data3 = mysql_query("SELECT t.*,b.title,m.m_name from transactions t, books b, members m where b.book_id = t.book_id and m.member_id = t.member_id order by t.t_id DESC")	
	return render_template('issue_books.html',data=data,data1=data1,data3=data3)

@app.route('/issue_book',methods=['POST'])
def issue_book():
	if request.method == 'POST':	
		book_id = request.form['book_id']
		member_id = request.form['member_id']
		issue_date = date.today()
		if book_id and member_id != '0':
			record = mysql_query("SELECT book_id,member_id,return_date from transactions where book_id = '{}' and member_id = '{}'".format(book_id,member_id))
			issues_of_books =  mysql_query("SELECT count(member_id) as total_issues_without_return from transactions where member_id = '{}' and return_date is NULL group by member_id".format(member_id))
			stock = mysql_query("SELECT title,stock from books where book_id = '{}'".format(book_id))
			m_name = mysql_query("SELECT m_name from members where member_id = '{}'".format(member_id))
			total_outstandings = mysql_query("SELECT sum(outstanding_amount) as total_outstandings from transactions where member_id = '{}' group by member_id".format(member_id))
			m_name = m_name[0]['m_name']
			title = stock[0]['title']
			
			if len(record) != 0 and record[0]['return_date'] == None :
				flash("Book already issued to "+m_name+" !" ,'warning')
			elif len(issues_of_books) != 0 and issues_of_books[0]['total_issues_without_return'] == 2:
				flash(m_name+" has already been issued 3 books ! Return some to proceed !" ,'danger')
			elif len(stock) != 0 and stock[0]['stock'] == 0:
				flash(title+" is Out of Stock" ,'warning')
			elif len(total_outstandings) != 0 and total_outstandings[0]['total_outstandings'] > 500:
				flash("Total Outstandings Exceeds ₹500"+m_name ,'danger')
			else:
				mysql_query("UPDATE books set stock = stock - {} where book_id = '{}'".format(1,book_id))
				mysql_query("INSERT into transactions(book_id,member_id,issue_date) values ('{}','{}','{}')".format(book_id,member_id,issue_date))
		if book_id or member_id == '0':
			return redirect(url_for('issue_books_page_load'))	
	return redirect(url_for('issue_books_page_load'))

@app.route('/book_return',methods=['POST'])
def book_return():
	if request.method == 'POST':
		book_id = request.form['book_id']
		member_id = request.form['member_id']
		rent_amount_to_collect = request.form['rent_amount_to_collect']
		rent_paid = request.form['rent_paid']
		return_date = date.today()
		t_id = request.form['t_id']
		mysql_query("UPDATE books set stock = stock + {} where book_id = '{}'".format(1,book_id))
		if rent_paid == "yes":
			mysql_query("UPDATE transactions t inner join members m on t.member_id = m.member_id set t.outstanding_amount = '{}', t.return_date = '{}', t.total_rent = '{}', t.rent_paid = '{}' where t.t_id = '{}'".format(0,return_date,rent_amount_to_collect,rent_paid,t_id))
			result = mysql_query("SELECT member_id as m_id,sum(total_rent) as total_rent_amount_paid_yet from transactions where rent_paid = '{}' and member_id = '{}'".format('yes',member_id))
			amount_paid_till_now = result[0]['total_rent_amount_paid_yet']
			m_id = result[0]['m_id']
			mysql_query("UPDATE members set total_amount_paid = '{}' where member_id = '{}'".format(amount_paid_till_now,m_id))
		else:
			mysql_query("UPDATE transactions t inner join members m on t.member_id = m.member_id set t.outstanding_amount = '{}', t.return_date = '{}', t.total_rent = '{}', t.rent_paid = '{}' where t.t_id = '{}'".format(rent_amount_to_collect,return_date,rent_amount_to_collect,rent_paid,t_id))
		return redirect(url_for('issue_books_page_load'))

@app.route('/outstanding_settlement',methods=['POST'])
def outstanding_settlement():
	if request.method == 'POST':
		t_id = request.form['t_id']
		book_id = request.form['book_id']
		member_id = request.form['member_id']
		m_name = request.form['m_name']
		outstanding_amount = request.form['outstanding_amount']
		rent_amount = request.form['rent_amount']
		new_amount = int(outstanding_amount) - int(rent_amount)
		if new_amount == 0:
			mysql_query("UPDATE transactions t inner join members m on t.member_id = m.member_id set t.outstanding_amount = '{}', t.rent_paid = '{}' where m.member_id = '{}' and  t.t_id = '{}'".format(new_amount,'yes',member_id,t_id))
			mysql_query("UPDATE books set stock = stock + {} where book_id = '{}'".format(1,book_id))
			result = mysql_query("SELECT member_id as m_id,sum(total_rent) as total_rent_amount_paid_yet from transactions where rent_paid = '{}' and member_id = '{}'".format('yes',member_id))
			amount_paid_till_now = result[0]['total_rent_amount_paid_yet']
			m_id = result[0]['m_id']
			mysql_query("UPDATE members set total_amount_paid = '{}' where member_id = '{}'".format(amount_paid_till_now,m_id))
			flash("Outstanding Amount Cleared for " +m_name ,'success')
		else:
			mysql_query("UPDATE transactions set outstanding_amount = '{}' where member_id = '{}' and t_id = '{}'".format(new_amount,member_id,t_id))
			mysql_query("UPDATE members set total_amount_paid =  total_amount_paid + '{}' where member_id = '{}'".format(rent_amount,member_id))
			flash("Adjustments done for " +m_name ,'info')
	return redirect(url_for('issue_books_page_load'))


@app.route('/reports',methods=['POST'])
def reports():
	if request.method == 'POST':
		if 'button2' in request.form:
			data = mysql_query("SELECT * from members order by total_amount_paid DESC")
			return render_template('index.html',data = data)
		if 'button1' in request.form:
			data2 = mysql_query("SELECT b.book_id,b.title,b.authors,b.publication_date,b.stock,b.publisher,b.ratings_count,count(t.book_id) from transactions t,books b where b.book_id = t.book_id group by t.book_id order by count(t.book_id) DESC")
			
			return render_template('index.html',data2 = data2)
	return render_template('index.html')

if __name__ == "__main__":
	app.run(port='8000', debug=True)