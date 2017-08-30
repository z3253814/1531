from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		name = request.form["name"]
		zID = int(request.form["zID"])
		description = request.form["desc"]
		#       user_input.append([name, zID, description])
		write(name, zID, description)
		return redirect(url_for('hello'))
	return render_template('index.html')

@app.route('/Hello')
def hello():
	user_input = [];
	read(user_input)
	return render_template('Hello.html', all_users=user_input)
    
def write(name, zID, desc):
	with open('example.csv','a') as csv_out:
		writer = csv.writer(csv_out)
		writer.writerow([name, zID, desc])
		
def read(user_input):
	with open('example.csv','r') as csv_in:
		reader = csv.reader(csv_in)
		for row in reader:
			user_input.append(row)
