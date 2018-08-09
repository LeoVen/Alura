# #
# operations.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 08/08/2018
#
# #

from visitor import Visitor


class Sum:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() + self.__right.eval()

	def visit(self, visitor):
		visitor.visit_sum(self)

	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right


class Sub:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() - self.__right.eval()

	def visit(self, visitor):
		visitor.visit_sub(self)

	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right

class Mult:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() * self.__right.eval()

	def visit(self, visitor):
		visitor.visit_mult(self)

	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right

class Div:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() / self.__right.eval()

	def visit(self, visitor):
		visitor.visit_div(self)

	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right

class Pow:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() ** self.__right.eval()

	def visit(self, visitor):
		visitor.visit_pow(self)

	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right

class Root:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() ** (1 / self.__right.eval())

	def visit(self, visitor):
		visitor.visit_root(self)

	@property
	def left(self):
		return self.__left

	@property
	def right(self):
		return self.__right

class Number:

	def __init__(self, number):
		self.__number = number

	def eval(self):
		return self.__number

	def visit(self, visitor):
		visitor.visit_number(self)


def main():
	
	a = 4
	b = -2
	c = 6
	d = 10

	# Our visitor
	visitor = Visitor()

	# Object of our operation
	result = Div(Sub(Div(Number(a), Number(b)), Sum(Number(c), Number(a))), Mult(Number(a), Sub(Number(b), Number(c))))
	result.visit(visitor)
	print("  = ", result.eval())

	# Another operation
	result = Root(Pow(Number(a), Number(d)), Number(a))
	result.visit(visitor)
	print("  = ", result.eval())

	# ???????
	result = Div(Mult(Sum(Mult(Root(Sub(Number(69), Number(-31)), Number(2)), Number(7)), Number(1)), Root(Sum(Number(100), Pow(Number(5), Sum(Number(1), Sub(Number(25), Mult(Number(6), Number(4)))))), Number(3))), Sub(Sum(Pow(Number(2), Number(10)), Number(-901)), Root(Sub(Pow(Number(12), Number(2)), Number(44)), Number(2))))
	result.visit(visitor)
	print("  = ", result.eval())


if __name__ == '__main__':
	main()
