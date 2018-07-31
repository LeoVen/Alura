# #
# taxes.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 29/07/2018
#
# #

from abc import ABC, abstractmethod

# Decorator
def IPVX(method):

	def wrapper(self, budget):
		return method(self, budget) + 50.0

	return wrapper

class Tax:

	def __init__(self, another_tax = None):
		self._another_tax = another_tax

	@abstractmethod
	def tax_calc(self, budget):
		pass

	def tax_calc_other(self, budget):

		if self._another_tax is None:
			return 0
		else:
			return self._another_tax.tax_calc(budget)
	

class TaxTemplate(ABC, Tax):

	def tax_calc(self, budget):

		if self.use_max_taxation(budget):
			return self.max_taxation(budget) + self.tax_calc_other(budget)
		else:
			return self.min_taxation(budget) + self.tax_calc_other(budget)

	@abstractmethod
	def use_max_taxation(self, budget):
		pass

	@abstractmethod
	def max_taxation(self, budget):
		pass

	@abstractmethod
	def min_taxation(self, budget):
		pass


class ISS(Tax):

	@IPVX
	def tax_calc(self, budget):
		return budget.value * 0.1 + self.tax_calc_other(budget)


class ICMS(Tax):
	
	@IPVX
	def tax_calc(self, budget):
		return budget.value * 0.06 + self.tax_calc_other(budget)


class IPI(Tax):

	def tax_calc(self, budget):
		return budget.value * 0.02


class ICPP(TaxTemplate):

	def use_max_taxation(self, budget):
		return budget.value > 500

	def max_taxation(self, budget):
		return budget.value * 0.07

	def min_taxation(self, budget):
		return budget.value * 0.05


class IKCV(TaxTemplate):

	def __has_item_gt_100(self, budget):

		for item in budget.get_items():
			
			if item.value > 100:
				return True
		
		return False

	def use_max_taxation(self, budget):
		return budget.value > 500 and self.__has_item_gt_100(budget)

	def max_taxation(self, budget):
		return budget.value * 0.1


	def min_taxation(self, budget):
		return budget.value * 0.06
