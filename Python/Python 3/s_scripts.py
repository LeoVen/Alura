# Random scripts

from math import factorial
from math import pi
from random import choice
from random import randint
from random import randrange

def main():
	for i in range(0, 32, 2):
		print("Hello", "World", sep=" ", end=" ")

	print("Hello", "World", sep=" ")

	n1 = 10
	n2 = "10"
	product = n1 * n2

	my_var = "{} X {} = {}".format(n1, n2, product)

	print(my_var)

	# break: goes out of loop
	# continue: goes to the next iteration

	n = 0

	for i in range(100):

		n += 1
		
		if (i % 2 == 0):
			continue
		
		print(i, end=" ")

	print("\n\n", n)

	# string formating:
	# help('FORMATTING')

	for i in range(20):
		print("Factorial of {:>2} is {:>20}".format(i, factorial(i)))

	print(pi)

	for i in range(10):
		print(randrange(0, 21, 4), end=" ")

	print(" ")

	for i in range(20):
		print(choice([1, 3, 5, 7]), end=" ")
	
	print(" ")

	print(r"One {1} Two {2} Three {3}")

	# float division /
	# integer division //

	print(11/3)
	print(11//3)

	print("HELLO WORLD".lower())
	print("lorem ipsum".upper())
	print("fire AND BLood".capitalize())

	print("Banana".endswith("na"))
	print("Banana".startswith("Ba"))

	print(" Au str ali a".strip(" "))
	print(" Au str ali a".replace(" ", ""))


if __name__ == "__main__":
	main()
