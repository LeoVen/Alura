# #
# case.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 22/08/2018
#
# #

input = gets.to_i

case input
when 1
	n = 30
when 2
	n = 500
when 3
	n = 100
when 4
	n = 30000
when 5..10
	n = 1313
else
	n = 0
end

puts n