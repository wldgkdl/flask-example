from flask import Flask 

application = Flask(__name__)

@application.route('/')    # default web page
def hello_world():
	return 'Welcome to Kevin & Kim factory'
