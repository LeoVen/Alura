# #
# visitor.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 08/08/2018
#
# #

class Visitor:

	def visit_sum(self, oper):
		print("(", end="")
		oper.left.visit(self)
		print(" + ", end="")
		oper.right.visit(self)
		print(")", end="")

	def visit_sub(self, oper):
		print("(", end="")
		oper.left.visit(self)
		print(" - ", end="")
		oper.right.visit(self)
		print(")", end="")

	def visit_mult(self, oper):
		print("(", end="")
		oper.left.visit(self)
		print(" * ", end="")
		oper.right.visit(self)
		print(")", end="")
	
	def visit_div(self, oper):
		print("(", end="")
		oper.left.visit(self)
		print(" / ", end="")
		oper.right.visit(self)
		print(")", end="")

	def visit_pow(self, oper):
		print("(", end="")
		oper.left.visit(self)
		print(" ** ", end="")
		oper.right.visit(self)
		print(")", end="")

	def visit_root(self, oper):
		print("(", end="")
		oper.left.visit(self)
		print(" ** ( 1 / ", end="")
		oper.right.visit(self)
		print("))", end="")

	def visit_number(self, number):

		if (number.eval() >= 0):
			print(number.eval(), end="")
		else:
			print("(", end="")
			print(number.eval(), end="")
			print(")", end="")
