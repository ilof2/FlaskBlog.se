from app import app
from flask import render_template


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404