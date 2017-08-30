from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input, output

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		numbers = (request.form["numbers"])
		return redirect(url_for('sort', numbers=numbers))
	return render_template('index.html')

@app.route('/sort/<numbers>')
def sort(numbers):
	user_input = list(map(int, numbers.split(',')))
	swapped = False
	length = len(user_input) - 1
	# output = []
	
	while not swapped:
		swapped = True
		for i in range(0, length):
			if user_input[i] > user_input[i+1]:
				user_input[i], user_input[i+1] = user_input[i+1], user_input[i]
				swapped = False
				output.append(user_input[:])	 
	return render_template('sort.html', numbers=output)
