from app import app
from flask import render_template


@app.route('/')
def index():
	names = ['Ilya', 'Sergey', 'Danik']
	return render_template('index.html', names = names)
