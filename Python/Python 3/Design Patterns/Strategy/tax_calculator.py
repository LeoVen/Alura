# #
# tax_calculator.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 24/07/2018
#
# #

# Strategy Pattern

from budget import Budget
from taxes import ISS, ICMS, IPI

class TaxCalculator:

	def calculate_tax(self, budget, tax_function):

		taxes = tax_function(budget)

		print(taxes)

	@property
	def tax():
		return self.__tax


def main():
	
	print("ICMS, ISS, IPI\n")

	money = Budget(500)

	calc = TaxCalculator()

	calc.calculate_tax(money, ICMS.tax_calc)
	calc.calculate_tax(money, ISS.tax_calc)
	calc.calculate_tax(money, IPI.tax_calc)


if __name__ == '__main__':
	main()