# #
# calculator.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 25/07/2018
#
# #

# Strategy Pattern

from budget import Budget, Item
from discounts import Discount_1, Discount_2, Discount_Null

class DiscountCalculator:

	def calculate_discount(self, budget):

		return Discount_1(Discount_2(Discount_Null())).calculate(budget)


def main():
	
	print("Discounts\n")

	budget = Budget()

	calc = DiscountCalculator()

	budget.add(Item('Item 1', 100))
	budget.add(Item('Item 2', 50))
	budget.add(Item('Item 3', 400))
	budget.add(Item('Item 4', 50))

	print("Total items    : {}".format(budget.total_items))
	print("Total value    : {}".format(budget.value))

	print("Total discount : {}".format(calc.calculate_discount(budget)))




if __name__ == '__main__':
	main()