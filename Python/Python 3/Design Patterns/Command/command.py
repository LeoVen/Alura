# #
# command.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 09/08/2018
#
# #

from abc import ABCMeta, abstractmethod
from datetime import date


class Request:

	def __init__(self, customer, value):
		self.__customer = customer
		self.__value = value
		self.__status = 'NEW'
		self.__completion_date = None

	def __str__(self):

		return (str(self.__customer) + " " + str(self.__value) + " : "
			 + str(self.__status) + " " + str(self.__completion_date))

	def pay(self):
		self.__status = 'PAID'

	def finalize(self):
		self.__completion_date = date.today()
		self.__status = 'DELIVERED'

	@property
	def customer(self):
		self.__customer

	@property
	def value(self):
		self.__value

	@property
	def status(self):
		self.__status

	@property
	def completion_date(self):
		self.__completion_date


class Command(metaclass = ABCMeta):

	@abstractmethod
	def execute(self):
		pass


class FinalizeRequest(Command):

	def __init__(self, request):
		self.__request = request

	def execute(self):
		self.__request.finalize()


class PayRequest(Command):

	def __init__(self, request):
		self.__request = request

	def execute(self):
		self.__request.pay()


class ProcessQueue:

	def __init__(self):
		self.__commands = []

	def add(self, command):
		self.__commands.append(command)

	def process(self):
		for command in self.__commands:
			command.execute()


if __name__ == "__main__":

	req0 = Request("Isaac Newton", 500)
	req1 = Request("Alan Turing", 300)
	req2 = Request("Ada Lovelace", 700)
	req3 = Request("Leonhard Euler", 200)

	proc_queue = ProcessQueue()

	c0 = PayRequest(req0)
	c1 = PayRequest(req1)
	c2 = FinalizeRequest(req1)
	c3 = FinalizeRequest(req2)

	proc_queue.add(c0)
	proc_queue.add(c1)
	proc_queue.add(c2)
	proc_queue.add(c3)

	proc_queue.process()

	print(req0)
	print(req1)
	print(req2)
	print(req3)
