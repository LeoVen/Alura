# #
# require.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 24/08/2018
#
# #

# require 'math'
require_relative 'math'

for i in 0..99

	puts "The number #{i} #{is_prime(i) ? "is" : "is not"} prime" 

end

i = 1

while i < 100

	print nth_prime(i)
	print " "

	i += 1

end