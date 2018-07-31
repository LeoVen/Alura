# #
# tax_calculator.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 29/07/2018
#
# #

from budget import Budget, Item
from taxes import ISS, ICMS, IPI, ICPP, IKCV

class TaxCalculator:

	def calculate_tax(self, budget, taxation):

		taxes = taxation.tax_calc(budget)

		print(taxes)

	@property
	def tax():
		return self.__tax


def main():

	calc = TaxCalculator()

	budget = Budget()

	budget.add(Item('Item 1', 100))
	budget.add(Item('Item 2', 50))
	budget.add(Item('Item 3', 400))
	budget.add(Item('Item 4', 50))

	calc.calculate_tax(budget, ICMS())
	calc.calculate_tax(budget, ISS())
	calc.calculate_tax(budget, IPI())

	calc.calculate_tax(budget, ICPP())
	calc.calculate_tax(budget, IKCV())


if __name__ == '__main__':
	main()