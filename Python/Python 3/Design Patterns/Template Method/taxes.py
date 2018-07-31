# #
# taxes.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 29/07/2018
#
# #

from abc import ABC, abstractmethod

class TaxTemplate(ABC):

	def tax_calc(self, budget):

		if self.use_max_taxation(budget):
			return self.max_taxation(budget)
		else:
			self.min_taxation(budget)

	@abstractmethod
	def use_max_taxation(self, budget):
		pass

	@abstractmethod
	def max_taxation(self, budget):
		pass

	@abstractmethod
	def min_taxation(self, budget):
		pass


class ISS:

	def tax_calc(self, budget):
		return budget.value * 0.1


class ICMS:
	
	def tax_calc(self, budget):
		return budget.value * 0.06


class IPI:

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
