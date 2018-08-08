# #
# app.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 07/08/2018
#
# #

# #####
# Builder X Factory
#
# Builder:
# When we have total control over the object and we can customize it if we wish
# to do so by passing different parameters
#
# Factory:
# We simply receive a pre-defined object, or in this case a fake connection.
# This is useful when we want all of our connections to have the same
# credentials of our real database
# #####

from conn_factory import ConnectionFactory

def main():
	
	connection = ConnectionFactory.get()

	print(connection)

if __name__ == '__main__':
	main()