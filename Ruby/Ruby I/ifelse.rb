# #
# ifelse.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 20/08/2018
#
# #
puts "Write a number"

number = gets.chomp.to_i

if number > 10
	puts "Your number is greater than 10!"
elsif number < 10
	puts "Your number is lesser than 10!"
else
	puts "Your number is 10!"
end

if number % 2 != 0
	puts "And your number is not divisible by 2!"
else
	puts "Your number is divisible by 2!"
end