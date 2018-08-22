# #
# loop.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 20/08/2018
#
# #

limit = 10

for x in 1..limit
	puts "Counting " + x.to_s # Needs to convert to string to use + sign
end

i = 0

for x in 1..limit
	puts x
	if x % 5 == 0
		break
	end
end

# Break if
for x in 1..limit
	puts x
	break if x % 4 == 0
end

secret_number = 65465
tries = 0
found = false

puts "Guess the secret number!"

while !found

	n = gets.chomp.to_i

	tries += 1

	if n < secret_number
		puts "Higher!"
	elsif n > secret_number
		puts "Lower!"
	else
		found = true
	end
end

puts "You guessed the number in " + tries.to_s + " tries"
