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

def squareImage(original):
	img = images.Image(original)
	if img.width > img.height:
		cropSize = float(img.width - img.height)/float(img.width*2)
		img.crop(cropSize,0.0,1.0 - cropSize,1.0)
	else:
		cropSize = float(img.height - img.width)/float(img.height*2)
		img.crop(0.0,cropSize,1.0,1.0 - cropSize)
	img.resize(220,220)
	return img.execute_transforms()

class Image(webapp.RequestHandler):
    def get(self):
        pointData = db.get(self.request.get("img_id"))
        if pointData.img:
			if self.request.get('tile') == "true":
				tile = squareImage(pointData.img)
				self.response.headers['Content-Type'] = "image/png"
				self.response.out.write(tile)
			else:
				self.response.headers['Content-Type'] = "image/png"
				self.response.out.write(pointData.img)
        else:
            self.redirect("resources/compass.png")

class MapPage(webapp.RequestHandler):
	def get(self):
		points = db.GqlQuery("SELECT * FROM Point ORDER BY date ASC")
		
		template_values = { 'points' : points }
		
		path = os.path.join(os.path.dirname(__file__), 'journey.html')
		self.response.out.write(template.render(path,template_values))
	
	
