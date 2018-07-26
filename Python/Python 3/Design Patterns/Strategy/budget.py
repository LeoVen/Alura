# #
# budget.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 24/07/2018
#
# #

class Budget:

	def __init__(self, value):
		self.__value = value

	@property
	def value(self):
		return self.__value
