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

app.config['MYSQL_DATABASE_HOST'] = 'sql6.freesqldatabase.com'
app.config['MYSQL_DATABASE_USER'] = 'sql6418281'
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = 'sql6418281'
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
	total_books_issued = mysql_query("SELECT count(t_id) as total_books_issued from transactions")
	total_books_issued = total_books_issued[0]['total_books_issued']
	registered_members = mysql_query("SELECT count(member_id) as registered_members from members")
	registered_members = registered_members[0]['registered_members']
	available_books = mysql_query("SELECT sum(stock) as available_books from books")
	available_books = available_books[0]['available_books']
	total_amount_recieved = mysql_query("SELECT sum(total_amount_paid) as total_amount_recieved from members")
	total_amount_recieved = total_amount_recieved[0]['total_amount_recieved']
	return render_template('index.html',total_books_issued = total_books_issued, registered_members = registered_members, available_books = available_books, total_amount_recieved = total_amount_recieved)

@app.route('/import_book', methods=['POST'])
def import_book():
	try:
		if request.method == 'POST':
			no_of_records = request.form['no_of_records']
			String_no_of_records = no_of_records
			no_of_records = int(no_of_records)
			title = request.form['title']
			authors = request.form['authors']
			isbn = request.form['isbn']
			publisher = request.form['publisher']
			list1 = []
			page = no_of_records/20
			rounded_value = math.ceil(page)
			#using loop for inserting n number of records 
			for b in range(1,rounded_value+1):
				list2 = []
				request_data = requests.get("https://frappe.io/api/method/frappe-library?page={}&title={}&authors={}&isbn={}&publisher={}".format(b,title,authors,isbn,publisher))
				list2 = request_data.json()
				list1.append(list2)	
			for a in list1:
				try:
					for b in range(0,no_of_records):
						book_id = a['message'][b]['bookID']
						data_check = mysql_query("SELECT book_id from books where book_id = '{}'".format(book_id))
						if len(data_check) == 0:
							connection = mysql.connect()
							cursor = connection.cursor()
							sql = "INSERT INTO books(book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,publication_date,publisher,ratings_count,text_reviews_count,stock,total_stock) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
							timestring = datetime.strptime(a['message'][b]['publication_date'],'%m/%d/%Y')
							dt = (a['message'][b]['bookID'],a['message'][b]['title'],a['message'][b]['authors'],a['message'][b]['average_rating'],a['message'][b]['isbn'],a['message'][b]['isbn13'],a['message'][b]['language_code'],a['message'][b]['  num_pages'],timestring,a['message'][b]['publisher'],a['message'][b]['ratings_count'],a['message'][b]['text_reviews_count'],no_of_records,no_of_records)
							cursor.execute(sql,dt)
							print(no_of_records)
							connection.commit()
						else:
							flash("The '"+title+"' book already exists ! try updating the stock.",'warning') 
					flash("The '"+title+"' book has been added successfully with '"+String_no_of_records+"' quantities in stock !",'success') 
				except:
					for b in range(1,no_of_records):
						book_id = a['message'][b]['bookID']
						data_check = mysql_query("SELECT book_id from books where book_id = '{}'".format(book_id))
						if len(data_check) == 0:
							connection = mysql.connect()
							cursor = connection.cursor()
							sql = "INSERT INTO books(book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,publication_date,publisher,ratings_count,text_reviews_count,stock,total_stock) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
							timestring = datetime.strptime(a['message'][b]['publication_date'],'%m/%d/%Y')
							dt = (a['message'][b]['bookID'],a['message'][b]['title'],a['message'][b]['authors'],a['message'][b]['average_rating'],a['message'][b]['isbn'],a['message'][b]['isbn13'],a['message'][b]['language_code'],a['message'][b]['  num_pages'],timestring,a['message'][b]['publisher'],a['message'][b]['ratings_count'],a['message'][b]['text_reviews_count'],no_of_records,no_of_records)
							cursor.execute(sql,dt)
							print(no_of_records)
							connection.commit()
						else:
							flash("The '"+title+"' book already exists ! try updating the stock",'warning') 
					flash("The '"+title+"' book has been added successfully with '"+String_no_of_records+"' quantities in stock !",'success') 
			return redirect(url_for('manage_books'))
	except:
			return redirect(url_for('manage_books'))


@app.route('/manage_books')
def manage_books():
	data = mysql_query("SELECT * from books order by title ASC")
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
		connection = mysql.connect()
		cursor = connection.cursor()
		query = "UPDATE books set title = %s, average_rating = %s, authors = %s, language_code = %s, publication_date = %s, publisher = %s, stock = %s where book_id = %s"
		dt = (title,average_rating,authors,language_code,publication_date,publisher,stock,book_id)
		cursor.execute(query,dt)
		connection.commit()
		updated_stock = mysql_query("SELECT stock from books where book_id = '{}'".format(book_id))
		stock = str(updated_stock[0]['stock'])
		flash("The '"+title+"' Book Updated Successfully ! updated stock is '"+stock+"'",'success')
	return redirect(url_for('manage_books'))

@app.route('/delete_book', methods=['POST'])
def delete_book():
	if request.method == 'POST':
		book_id = request.form['book_id']
		mysql_query("DELETE from books where book_id = '{}'".format(book_id))
		flash("Book Deleted Successfuly !",'warning')
	return redirect(url_for('manage_books'))


@app.route('/manage_members')
def manage_members():
	data = mysql_query("SELECT * from members order by m_name")
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
		flash("Member Updated Successfully !",'success')
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

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/terms_checked',methods=['POST'])
def terms_checked():
    return redirect(url_for('issue_books_page_load'))
			
@app.route('/issue_books_page_load')
def issue_books_page_load():
	data = mysql_query("SELECT book_id,title from books")
	data1 = mysql_query("SELECT member_id,m_name from members")
	data3 = mysql_query("SELECT t.*,b.title,m.m_name from transactions t, books b, members m where b.book_id = t.book_id and m.member_id = t.member_id order by t.t_id DESC")	
	return render_template('issue_books.html',data=data,data1=data1,data3=data3)

@app.route('/issue_book',methods=['POST'])
def issue_book():
	try:
		if request.method == 'POST':	
			book_id = request.form['book_id']
			member_id = request.form['member_id']
			issue_date = date.today()
			print(book_id)
			print(member_id)
			if book_id and member_id != 0:
				record = mysql_query("SELECT book_id,member_id,return_date from transactions where book_id = '{}' and member_id = '{}'".format(book_id,member_id))
				issues_of_books =  mysql_query("SELECT count(member_id) as total_issues_without_return from transactions where member_id = '{}' and return_date is NULL group by member_id".format(member_id))
				stock = mysql_query("SELECT title,stock from books where book_id = '{}'".format(book_id))
				m_name = mysql_query("SELECT m_name from members where member_id = '{}'".format(member_id))
				total_outstandings = mysql_query("SELECT sum(outstanding_amount) as total_outstandings from transactions where member_id = '{}' group by member_id".format(member_id))
				m_name = m_name[0]['m_name']
				title = stock[0]['title']
				
				if len(record) != 0 and record[0]['return_date'] == None :
					flash(title+" book is already issued to "+m_name+" !" ,'warning')
				elif len(issues_of_books) != 0 and issues_of_books[0]['total_issues_without_return'] == 2:
					flash(m_name+" has already been issued 2 books which are not returned yet ! Return some to proceed." ,'danger')
				elif len(stock) != 0 and stock[0]['stock'] == 0:
					flash(title+" book is Out of Stock ! It will be right back soon." ,'warning')
				elif len(total_outstandings) != 0 and total_outstandings[0]['total_outstandings'] > 500:
					flash("Total Outstandings for "+m_name+" Exceeds ₹500 ! Clear the outstanding amount." ,'danger')
				else:
					mysql_query("UPDATE books set stock = stock - {} where book_id = '{}'".format(1,book_id))
					mysql_query("INSERT into transactions(book_id,member_id,issue_date) values ('{}','{}','{}')".format(book_id,member_id,issue_date))
		return redirect(url_for('issue_books_page_load'))
	except:
		flash("Please Select Valid input" ,'danger')
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


@app.route('/report1')
def report1():
	data = mysql_query("SELECT * from members order by total_amount_paid DESC")
	return render_template('reports.html',data = data)

@app.route('/report2')
def report2():
	data2 = mysql_query("SELECT b.book_id,b.title,b.authors,b.publication_date,b.stock,b.total_stock,b.publisher,b.ratings_count,count(t.book_id) from transactions t,books b where b.book_id = t.book_id group by t.book_id order by count(t.book_id) DESC")
	print(data2)
	return render_template('reports.html',data2 = data2)


if __name__ == "__main__":
	app.run(debug=True)