# #
# conn_factory.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 07/08/2018
#
# #

# Just making a fake connection
class MySQLdb:

	@staticmethod
	def connect(host, user, passwd, db):

		return tuple([host, user, passwd, db])

class ConnectionFactory:

	@staticmethod
	def get():

		return MySQLdb.connect(
			host = 'localhost',
			user = 'root',
			passwd = 'toor',
			db = 'alura')