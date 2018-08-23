# #
# loop1.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 22/08/2018
#
# #

x = 0

# Infinit loop until break
loop do
	x += 1
	puts x
	break if x >= 10
end

puts "\n#{x}\n\n"

x = 0

begin
	x += 1
	puts x
end until x >= 10

puts "\n#{x}\n\n"

# i is a local variable
(1..10).each do |i|
	puts i
end

puts "\n"

# Next
for x in 1..1000
	if x % 91 == 0
		puts x
	else
		next # goes to the next iteration
	end
end