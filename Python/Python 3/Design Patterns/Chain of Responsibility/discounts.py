# #
# taxes.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 25/07/2018
#
# #

class Discount_1:

	def __init__(self, next_discount):

		self.__next_discount = next_discount


	def calculate(self, budget):

		if budget.total_items > 5:
			return budget.value * 0.1
		return self.__next_discount.calculate(budget)


class Discount_2:

	def __init__(self, next_discount):

		self.__next_discount = next_discount

	def calculate(self, budget):

		if budget.value > 500:
			return budget.value * 0.07
		return self.__next_discount.calculate(budget)


class Discount_Null:

	def calculate(self, budget):

		return 0