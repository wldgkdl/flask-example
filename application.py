from flask import Flask, render_template
import os

application = Flask(__name__)

@application.route('/')    # default web page
def welcome_page():
	return render_template('index.html')
	# return 'Welcome to Kevin & Kim factory. This code comes from git now'


