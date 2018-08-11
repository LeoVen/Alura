from django.db import models

# Create your models here.

class Profile(object):

	def __init__(self, name='', email='', phone=''):
		self.name = name
		self.email = email
		self.phone = phone