import cgi
import datetime
import urllib
import os
import wsgiref.handlers

from model import Point

from google.appengine.ext import db,webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import images
	
class DataEntry(webapp.RequestHandler):
	def get(self):
		points = db.GqlQuery("SELECT * FROM Point ORDER BY date ASC")
		
		template_values = { 'points' : points }
		
		path = os.path.join(os.path.dirname(__file__), 'input.html')
		self.response.out.write(template.render(path,template_values))

		
class Submission(webapp.RequestHandler):
	def post(self):
		
		point = Point()
		point.title = self.request.get('title')
		
		if self.request.get('path'):
			point.path = True
		else:
			point.path = False
		
		point.content = cgi.escape(self.request.get('content')).replace('\r\n','<br>').replace('\n','<br>');
		
		point.lat = float(self.request.get('lat'))
		point.lng = float(self.request.get('lng'))
		
		dt = self.request.get('visit')
		if dt:
			point.date = datetime.datetime.strptime(dt,"%Y-%m-%d")
		else:
			point.date = datetime.datetime.now()
			
		point.dateStr = point.date.strftime('%b %d, %Y')
		
		if self.request.get('image'):
			point.img = db.Blob(images.resize(self.request.get('image'),500,500))
		
		point.put()
		self.redirect('/admin')
		

class Delete(webapp.RequestHandler):
	def get(self):
		key = self.request.get('key')
		db.delete(key)
		
		self.redirect('/admin')