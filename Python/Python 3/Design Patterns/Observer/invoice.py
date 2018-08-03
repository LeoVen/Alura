# #
# invoice.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 02/08/2018
#
# #
from datetime import date
from observer import send_to_print, send_to_database, send_to_email
import builder


class Invoice:

	def __init__(self, social_cause, ein, items, date=date.today(), details='', observers=[]):
		self.__social_cause = social_cause
		self.__ein = ein
		self.__items = items
		self.__date = date
		if len(details) > 20:
			raise Exception('Datails can not have more than 20 characters')
		self.__details = details
		self.__observers = observers

	@property
	def social_cause(self):
		return self.__social_cause

	@property
	def ein(self):
		return self.__ein

	@property
	def date(self):
		return self.__date

	@property
	def details(self):
		return self.__details

	def send(self):

		for obs in self.__observers:
			obs(self)

	def __str__(self):

		return ("Invoice [" + str(self.date) + "]: " + str(self.social_cause) +
		 " (" + str(self.ein) + ") " + str(self.__items) + " \n" + str(self.details))

	__repr__ = __str__


class Item:

	def __init__(self, name, value):
		self.__name = name
		self.__value = value

	@property
	def value(self):
		return self.__value

	@property
	def name(self):
		return self.__name

	def __str__(self):

		return "{Item: " + str(self.name) + " $" + str(self.value) + "}"

	__repr__ = __str__


def main():

	items = [Item("Car", 23000), Item("House", 500000)]
	
	# Multiple observers can be added
	observers = [send_to_print, send_to_database, send_to_email]

	invoice = builder.Invoice_Builder().social_cause("Commerce").ein("554-98.66549-8").items(items).observers(observers).build()

	print(invoice)

	invoice.send()


if __name__ == '__main__':
	main()