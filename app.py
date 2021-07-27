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
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DATABASE_DB')
mysql = MySQL(app)

#MySQL Query Driver function
def mysql_query(sql):
	connection = mysql.connect()
	cursor = connection.cursor()
	print(sql)
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
	else:
		cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return None
	
#Homepage
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

#Import book from API
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
			#using loop for searching records on pages 
			for b in range(1,rounded_value+1):
				list2 = []
				request_data = requests.get("https://frappe.io/api/method/frappe-library?page={}&title={}&authors={}&isbn={}&publisher={}".format(b,title,authors,isbn,publisher))
				list2 = request_data.json()
				list1.append(list2)	
			for a in list1:
				try:
					for b in range(0,no_of_records):
						book_id = a['message'][b]['bookID']
						book_title = a['message'][b]['title']
						book_data_check = mysql_query("SELECT book_id from books where book_id = '{}'".format(book_id))
						if len(book_data_check) == 0:
							timestring = datetime.strptime(a['message'][b]['publication_date'],'%m/%d/%Y')
							converted_book_title = a['message'][b]['title'].replace("'","\\'")
							authors_name = a['message'][b]['authors'].replace("'","\\'")
							publishers_name = a['message'][b]['publisher'].replace("'","\\'")
							mysql_query("INSERT INTO books(book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,publication_date,publisher,ratings_count,text_reviews_count,stock,total_stock) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a['message'][b]['bookID'],converted_book_title,authors_name,a['message'][b]['average_rating'],a['message'][b]['isbn'],a['message'][b]['isbn13'],a['message'][b]['language_code'],a['message'][b]['  num_pages'],timestring,publishers_name,a['message'][b]['ratings_count'],a['message'][b]['text_reviews_count'],no_of_records,no_of_records))
							flash("The '"+book_title+"' book has been added successfully with '"+String_no_of_records+"' quantities in stock !",'success') 
							break
						else:
							flash("The '"+book_title+"' book already exists ! try updating the stock from the update section.",'warning') 
							break
				except:
					flash("The '"+title+"' book doesn't exists",'danger')
					return redirect(url_for('manage_books'))
				return redirect(url_for('manage_books'))			
	except:
		return redirect(url_for('manage_books'))

#Manage Books Page Load
@app.route('/manage_books')
def manage_books():
	book_titles = mysql_query("SELECT * from books order by title ASC")
	languages_codes = mysql_query("SELECT language_code from books")
	return render_template('manage_books.html',book_titles=book_titles,languages_codes=languages_codes)

#Update Books alongwith stock updation
@app.route('/update_book', methods=['POST'])
def update_book():
	if request.method == 'POST':
		book_id = request.form['book_id']
		title = request.form['title']
		converted_title = title.replace("'","\\'")
		average_rating = request.form['average_rating']
		authors = request.form['authors'].replace("'","\\'")
		language_code = request.form['language_code']
		publication_date = request.form['publication_date']
		publisher = request.form['publisher'].replace("'","\\'")
		stock = request.form['stock']
		mysql_query("UPDATE books set title = '{}', average_rating = '{}', authors = '{}', language_code = '{}', publication_date = '{}', publisher = '{}', stock = '{}', total_stock = '{}' where book_id = '{}'".format(converted_title,average_rating,authors,language_code,publication_date,publisher,stock,stock,book_id))
		flash("The '"+title+"' Book Updated Successfully !",'success')
	return redirect(url_for('manage_books'))

#Delete Book
@app.route('/delete_book', methods=['POST'])
def delete_book():
	if request.method == 'POST':
		book_id = request.form['book_id']
		mysql_query("DELETE from books where book_id = '{}'".format(book_id))
		flash("Book Deleted Successfuly !",'warning')
	return redirect(url_for('manage_books'))

#Manage Members Page Load
@app.route('/manage_members')
def manage_members():
	member_details = mysql_query("SELECT * from members order by member_id DESC")
	return render_template('manage_members.html',member_details=member_details)

#Add Member
@app.route('/add_member', methods=['POST'])
def add_member(): 
	if request.method == 'POST' and 'm_name' in request.form and 'mobile' in request.form and 'email_id' in request.form and 'address' in request.form :
		m_name = request.form['m_name']
		mobile = request.form['mobile']
		email_id = request.form['email_id']
		m_address = request.form['address'].replace("'","\\'")
		member_data_check = mysql_query("SELECT member_id from members where email_id='{}' OR mobile='{}'".format(email_id,mobile))
		if len(member_data_check) == 0:
			mysql_query("INSERT INTO members(m_name,mobile,email_id,m_address) values ('{}', '{}', '{}', '{}')".format(m_name,mobile,email_id,m_address))
			flash("Member Added Successfully !",'info')	
		else:
			flash('Member Already Exists', 'danger')
			return redirect(url_for('manage_members'))
	elif request.method == 'POST':
		flash('Please fill the form !','error')
	return redirect(url_for('manage_members'))

#Update Member
@app.route('/update_member',methods=['POST'])
def update_member():
	if request.method == 'POST':
		member_id = request.form['member_id']
		m_name = request.form['m_name']
		mobile = request.form['mobile']
		email_id = request.form['email_id']
		m_address = request.form['address'].replace("'","\\'")
		mysql_query("UPDATE members set m_name = '{}', mobile = '{}', email_id = '{}', m_address = '{}' where member_id = '{}'".format(m_name,mobile,email_id,m_address,member_id))
		flash("'"+m_name+"'s details Updated Successfully !",'success')
	return redirect(url_for('manage_members'))

#Delete Member
@app.route('/delete_member',methods=['POST'])
def delete_member():
	if request.method == 'POST':
		member_id = request.form['member_id']
		mysql_query("DELETE from members where member_id = '{}'".format(member_id))
		flash("Member Deleted Successfuly !",'warning')
	return redirect(url_for('manage_members'))

#Terms of Service Page Load
@app.route('/terms')
def terms():
    return render_template('terms.html')

#Terms Checked page redirection
@app.route('/terms_checked',methods=['POST'])
def terms_checked():
    return redirect(url_for('issue_books_page_load'))

#Page Load Issue Books		
@app.route('/issue_books_page_load')
def issue_books_page_load():
	book_details = mysql_query("SELECT book_id,title from books")
	member_details = mysql_query("SELECT member_id,m_name from members")
	transaction_details = mysql_query("SELECT t.*,b.title,m.m_name from transactions t, books b, members m where b.book_id = t.book_id and m.member_id = t.member_id order by t.t_id DESC")	
	return render_template('issue_books.html',book_details=book_details,member_details=member_details,transaction_details=transaction_details)

#Issue Books to Members meanwhile checking several conditions
@app.route('/issue_book',methods=['POST'])
def issue_book():
	try:
		if request.method == 'POST':	
			book_id = request.form['book_id']
			member_id = request.form['member_id']
			issue_date = date.today()
			if book_id and member_id != 0:
				book_issued_data_check = mysql_query("SELECT book_id,member_id,return_date from transactions where book_id = '{}' and member_id = '{}'".format(book_id,member_id))
				book_issued_times =  mysql_query("SELECT count(member_id) as total_issues_without_return from transactions where member_id = '{}' and return_date is NULL group by member_id".format(member_id))
				stock = mysql_query("SELECT title,stock from books where book_id = '{}'".format(book_id))
				m_name = mysql_query("SELECT m_name from members where member_id = '{}'".format(member_id))
				total_outstandings = mysql_query("SELECT sum(outstanding_amount) as total_outstandings from transactions where member_id = '{}' group by member_id".format(member_id))
				m_name = m_name[0]['m_name']
				title = stock[0]['title']
				
				if len(book_issued_data_check) != 0 and book_issued_data_check[0]['return_date'] == None :
					flash("'"+title+"' book is already issued to '"+m_name+"' !" ,'warning')
				elif len(book_issued_times) != 0 and book_issued_times[0]['total_issues_without_return'] == 2:
					flash("'"+m_name+"' has already been issued 2 books which are not returned yet ! Return some to proceed." ,'danger')
				elif len(stock) != 0 and stock[0]['stock'] == 0:
					flash("The '"+title+"' book is Out of Stock ! It will be right back soon." ,'warning')
				elif len(total_outstandings) != 0 and total_outstandings[0]['total_outstandings'] > 500:
					flash("Total Outstandings for '"+m_name+"' Exceeds ₹500 ! Clear the outstanding amount." ,'danger')
				else:
					mysql_query("UPDATE books set stock = stock - {} where book_id = '{}'".format(1,book_id))
					mysql_query("INSERT into transactions(book_id,member_id,issue_date) values ('{}','{}','{}')".format(book_id,member_id,issue_date))
					flash("'"+title+ "' book successfully issued to '"+m_name+"'",'success')
		return redirect(url_for('issue_books_page_load'))
	except:
		flash("Please Select Valid input" ,'danger')
		return redirect(url_for('issue_books_page_load'))

#Return Book
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
			flash("Book Returned Successfully",'success')
		else:
			mysql_query("UPDATE transactions t inner join members m on t.member_id = m.member_id set t.outstanding_amount = '{}', t.return_date = '{}', t.total_rent = '{}', t.rent_paid = '{}' where t.t_id = '{}'".format(rent_amount_to_collect,return_date,rent_amount_to_collect,rent_paid,t_id))
			flash("Book Returned Successfully, Amount transferred to Outstanding Amount",'info')
		return redirect(url_for('issue_books_page_load'))

#Outstanding Amount Settlement
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
			flash("Outstanding Amount Cleared for '"+m_name+"'" ,'success')
		else:
			mysql_query("UPDATE transactions set outstanding_amount = '{}' where member_id = '{}' and t_id = '{}'".format(new_amount,member_id,t_id))
			mysql_query("UPDATE members set total_amount_paid =  total_amount_paid + '{}' where member_id = '{}'".format(rent_amount,member_id))
			flash("Adjustments done for '"+m_name+"'" ,'info')
	return redirect(url_for('issue_books_page_load'))

#Report1 - Highest Paying Customer
@app.route('/highest_paying_customer_report')
def highest_paying_customer_report():
	highest_paying_customers = mysql_query("SELECT * from members order by total_amount_paid DESC")
	return render_template('reports.html',highest_paying_customers = highest_paying_customers)

#Report 2 - Most Pupular Book
@app.route('/most_popular_book_report')
def most_popular_book_report():
	most_popular_book = mysql_query("SELECT b.book_id,b.title,b.authors,b.publication_date,b.stock,b.total_stock,b.publisher,b.ratings_count,count(t.book_id) from transactions t,books b where b.book_id = t.book_id group by t.book_id order by count(t.book_id) DESC")
	return render_template('reports.html',most_popular_book = most_popular_book)

#App runner
if __name__ == "__main__":
	app.run(debug=True)