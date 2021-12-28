from flask import Flask
from flask import render_template, request
import numpy as np
import os
from werkzeug.utils import secure_filename
import utils



app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['FILE_UPLOADS'] = "./"
app.config['UPLOAD_FOLDER'] = "./"

@app.route('/')
def main():
	return render_template('upload.html')

@app.route('/import', methods=['POST'])
def importer():
	f = request.files['file']
	f.save(secure_filename(f.filename))
	df = utils.read_excel(secure_filename(f.filename))

	return render_template('main.html', 
							employees_count=utils.employees_count(df), 
							hours_count=utils.hours_count(df), 
							bookings_count=utils.bookings_count(df), 
							hours_per_employee=int(utils.hours_count(df) / utils.employees_count(df)),
							project_values=utils.project_values(df),
							project_labels=utils.project_labels(df),
							project_color='rgba(255, 56, 96, 0.4)',
							admin_values=utils.admin_values(df),
							admin_labels=utils.admin_labels(df),
							admin_color='rgba(0, 205, 175, 0.4)',
							operations_values=utils.operations_values(df),
							operations_labels=utils.operations_labels(df),
							operations_color='rgba(50, 115, 220, 0.4)',
							legend="Booked Hours",
							employees=utils.employees(df)
							)

@app.route('/preferences')
def preferences():
	return render_template('preferences.html')

if __name__ == "__main__":
	app.run(port=5000, debug=True)