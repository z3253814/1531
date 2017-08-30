from flask import Flask, redirect, render_template, request, url_for
from server import app, calculation, output
import csv, math

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		calc_input = (request.form["calc"])
		if calc_input == "=":
			try:
				output[0]= str(eval(calculation[0]))
				calculation[0] = output[0]
			except SyntaxError:
				output[0] = "Math error"
				calculation[0] = ""			
			return render_template('calc.html', calculation=output)
		elif calc_input =="CE":
			calculation[0] = ""
		elif calc_input == "C":
			calculation[0] = calculation[0][:-1]
		elif calc_input == "tan":
			val = int(eval(calculation[0]))
			output[0] = math.tan(val)
			calculation[0] = str(output[0])
			return render_template('calc.html', calculation=output)
		elif calc_input == "sin":
			val = int(eval(calculation[0]))
			output[0] = math.sin(val)
			calculation[0] = str(output[0])
			return render_template('calc.html', calculation=output)
		elif calc_input == "cos":
			val = int(eval(calculation[0]))
			output[0] = math.cos(val)
			calculation[0] = str(output[0])
			return render_template('calc.html', calculation=output)
		elif calc_input == "log":
			val = int(eval(calculation[0]))
			if output[0] == 0:
				output[0] = "Undefined"
				calculation[0] = ""
				return render_template('calc.html', calculation=output)
			output[0] = math.log(val)
			calculation[0] = str(output[0])
			return render_template('calc.html', calculation=output)
		elif calc_input == "sqrt":
			val = int(eval(calculation[0]))
			output[0] = math.sqrt(val)
			calculation[0] = str(output[0])
			return render_template('calc.html', calculation=output)
		else:
			calculation[0] = calculation[0] + calc_input
		
		return render_template('calc.html', calculation=calculation)
		
	return render_template('calc.html')



