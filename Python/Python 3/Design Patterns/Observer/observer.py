# #
# observer.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 02/08/2018
#
# #

def send_to_print(invoice):
	print("Printing               " + str(invoice))

def send_to_database(invoice):
	print("Saving into database   " + str(invoice))

def send_to_email(invoice):
	print("Sending to email       " + str(invoice))