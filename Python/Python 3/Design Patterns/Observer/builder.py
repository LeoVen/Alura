# #
# builder.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 02/08/2018
#
# #
from datetime import date
from invoice import Invoice

class Invoice_Builder:

	def __init__(self):
		self.__social_cause = None
		self.__ein = None
		self.__items = None
		self.__date = None
		self.__details = None
		self.__observers = None

	def social_cause(self, social_cause):

		self.__social_cause = social_cause
		return self

	def ein(self, ein):

		self.__ein = ein
		return self

	def items(self, items):

		self.__items = items
		return self
	
	def date(self, date):

		self.__date = date
		return self

	def details(self, details):

		self.__details = details
		return self

	def observers(self, observers):

		self.__observers = observers
		return self

	def build(self):

		if self.__social_cause is None:
			raise Exception("Social Cause must not be empty")
		if self.__ein is None:
			raise Exception("EIN must not be empty")
		if self.__items is None:
			raise Exception("Items must not be emtpy")
		if self.__date is None:
			self.__date = date.today()
		if self.__details is None:
			self.__details = ''
		if self.__observers is None:
			self.__observers = []
		
		return Invoice(	social_cause=self.__social_cause, ein=self.__ein,
		 				items=self.__items, date=self.__date, details=self.__details,
						observers=self.__observers)
