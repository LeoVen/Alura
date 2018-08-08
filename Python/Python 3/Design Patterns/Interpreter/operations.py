# #
# operations.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 07/08/2018
#
# #


class Sum:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() + self.__right.eval()


class Sub:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() - self.__right.eval()


class Mult:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() * self.__right.eval()


class Div:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() / self.__right.eval()


class Pow:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() ** self.__right.eval()


class Root:

	def __init__(self, left, right):
		self.__left = left
		self.__right = right

	def eval(self):
		return self.__left.eval() ** (1 / self.__right.eval())


class Number:

	def __init__(self, number):
		self.__number = number

	def eval(self):
		return self.__number


def main():
	
	a = 4
	b = -2
	c = 6
	d = 10

	# [(a + b) * (a - b)] / 2
	result = Div(Mult(Sum(Number(a), Number(b)), Sub(Number(a), Number(b))), Number(2)).eval()

	print(result)
	print(str(((a + b) * (a - b)) / 2))
	print(" ")

	# ((a / b) - (c + a)) / (a * (b - c))
	result = Div(Sub(Div(Number(a), Number(b)), Sum(Number(c), Number(a))), Mult(Number(a), Sub(Number(b), Number(c)))).eval()

	print(result)
	print(((a / b) - (c + a)) / (a * (b - c)))
	print(" ")

	# (a * b * c) / d
	result = Div(Mult(Mult(Number(a), Number(b)), Number(c)), Number(d)).eval()

	print(result)
	print((a * b * c) / d)
	print(" ")

	# b ** d

	result = Pow(Number(b), Number(d)).eval()

	print(result)
	print(b ** d)
	print(" ")

	# (c ** a) ** (1 / d)

	result = Root(Pow(Number(c), Number(a)), Number(d)).eval()

	print(result)
	print((c ** a) ** (1 / d))
	print(" ")

	# (a ** d) ** (1 / a)

	result = Root(Pow(Number(a), Number(d)), Number(a)).eval()

	print(result)
	print((a ** d) ** (1 / a))
	print(" ")


if __name__ == '__main__':
	main()
