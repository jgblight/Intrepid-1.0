import cgi
import datetime
import urllib
import os
import wsgiref.handlers

from input import DataEntry, Submission, Delete
from journey import MapPage, Image

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

application = webapp.WSGIApplication([('/admin',DataEntry),('/submit',Submission),('/',MapPage),('/img',Image),('/del',Delete)], debug=True)

def main():
	run_wsgi_app(application)
	
if __name__ == '__main__':
	main()