import cgi
import datetime
import urllib
import os
import wsgiref.handlers

from google.appengine.ext import db

class Point(db.Model):
	path = db.BooleanProperty()
	date = db.DateTimeProperty()
	dateStr = db.StringProperty()
	title = db.StringProperty()
	content = db.StringProperty(multiline=True)
	lat = db.FloatProperty()
	lng = db.FloatProperty()
	img = db.BlobProperty()