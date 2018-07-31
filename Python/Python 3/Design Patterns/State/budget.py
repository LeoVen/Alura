# #
# budget.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 30/07/2018
#
# #

from abc import ABC, abstractmethod

class BudgetState(ABC):

	@abstractmethod
	def apply_extra_discount(self, budget):
		pass

	@abstractmethod
	def approve(self, budget):
		pass

	@abstractmethod
	def reject(self, budget):
		pass

	@abstractmethod
	def finalize(self, budget):
		pass


class OnApproval(BudgetState):

	def apply_extra_discount(self, budget):
		budget.add_extra_discount(budget.value * 0.02)

	def approve(self, budget):
		budget.current_state = Approved()

	def reject(self, budget):
		budget.current_state = Rejected()

	def finalize(self, budget):
		raise Exception("On approval budget can't go directly to finalized")


class Approved(BudgetState):

	def apply_extra_discount(self, budget):
		budget.add_extra_discount(budget.value * 0.05)

	def approve(self, budget):
		raise Exception("Budget already approved")

	def reject(self, budget):
		raise Exception("Approved budget can't be rejected")

	def finalize(self, budget):
		budget.current_state = Finalized()


class Rejected(BudgetState):

	def apply_extra_discount(self, budget):
		raise Exception("Disapproved budgets won't get any discount")

	def approve(self, budget):
		raise Exception("Rejected budget can't be approved")

	def reject(self, budget):
		raise Exception("Budget already rejected")

	def finalize(self, budget):
		budget.current_state = Finalized()


class Finalized(BudgetState):

	def apply_extra_discount(self, budget):
		raise Exception("Finalized budgets won't get any discount")

	def approve():
		raise Exception("Can't change the state of a finalized budget")

	def reject():
		raise Exception("Can't change the state of a finalized budget")

	def finalize():
		raise Exception("Can't change the state of a finalized budget")


class Budget:

	def __init__(self):
		self.__items = []
		self.current_state = OnApproval()
		self.__extra_discount = 0

	@property
	def value(self):
		total = 0.0
		for item in self.__items:
			total += item.value
		return total

	def get_items(self):
		return tuple(self.__items)

	@property
	def total_items(self):
		return len(self.__items)

	def add(self, item):
		self.__items.append(item)

	@property
	def extra_discount(self):
		return self.__extra_discount

	def add_extra_discount(self, discount):
		self.__extra_discount += discount

	def apply_extra_discount(self):
		self.current_state.apply_extra_discount(self)

	def approve(self):
		self.current_state.approve(self)

	def reject(self):
		self.current_state.reject(self)

	def finalize(self):
		self.current_state.finalize(self)


class Item:

	def __init__(self, name, value):
		self.__name = name
		self.__value = value

	@property
	def value(self):
		return self.__value

	@property
	def name(self):
		return self.__name


def main():
	
	budget = Budget()

	budget.add(Item('Item 1', 100))
	budget.add(Item('Item 2', 50))
	budget.add(Item('Item 3', 400))
	budget.add(Item('Item 4', 50))

	budget.apply_extra_discount()

	print(budget.extra_discount)

	budget.approve()
	budget.finalize()


if __name__ == '__main__':
	main()