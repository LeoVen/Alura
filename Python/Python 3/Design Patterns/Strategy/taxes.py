# #
# taxes.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 24/07/2018
#
# #

class ISS:

	@staticmethod
	def tax_calc(budget):
		return budget.value * 0.1


class ICMS:
	
	@staticmethod
	def tax_calc(budget):
		return budget.value * 0.06


class IPI:

	@staticmethod
	def tax_calc(budget):
		return budget.value * 0.02

