# #
# func.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 21/08/2018
#
# #

def hello_world
	puts "Hello World!"
end

def power(a, b)

	r = a

	for x in 1..b
		r *= a
	end

	return r
end

def factorial(a)
	return 1 if a <= 1
	return factorial(a - 1) * a
end

num = power(5, 3)

puts power(2, 10)
puts power(3, 5)
puts num

hello_world()

for i in 0..10
	puts factorial(i)
end