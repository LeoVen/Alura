# #
# hangman.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 22/08/2018
#
# #

def pick_random_word()
	
	pool = ["apple", "house", "lion", "king kong", "alan turing"]

	hint = ["A fruit", "A place", "An animal", "Giant monster", "Famous computer scientist"]

	r = rand(pool.length)

	return pool[r], hint[r]
end

def get_dif(x)
	case x
	when 1
		return 12
	when 2
		return 8
	when 3
		return 4
	else
		return 12
	end
end

def game()

	puts "Choose game difficulty (1, 2, 3)"

	dif = gets.chomp.to_i

	tries = get_dif(dif)

	word_found = false

	info = pick_random_word()

	word = info[0]
	word_len = word.length

	puts "New challenge! A word with #{word_len} letters"
	puts "Hint: #{info[1]}"
	
	correct = Array.new(word_len, false)
	
	for i in 0..word_len - 1
		if word[i] == " "
			correct[i] = true
		end
	end

	tried_letters = []

	while !word_found && tries > 0

		for i in 0..word_len - 1
			if correct[i]
				print word[i]
			else
				print "_"
			end
		end
	
		print "\n\nTries #{tries} > "
	
		guess = gets.chomp.strip.downcase

		if guess.length == 1
			if tried_letters.include? guess
				puts "You already tried #{guess}\n"
			else
				tried_letters << guess
				tries -= 1
			end
	
			for i in 0..word_len - 1
				if guess.strip == word[i].strip
					correct[i] = true
				end
			end
		else
			if guess == word
				word_found = true
				break
			else
				break
			end
		end

		# If everything is correct
		if correct.all? { |x| x == true }
			word_found = true
			break
		end

	end

	if !word_found
		puts "You lost!"
	else
		puts "You won!"
	end

	puts "Would you like to play again? (Y/N)"
	choice = gets.chomp

	if choice.upcase == "Y"
		return true
	else
		return false
	end

end


puts "Welcome to hangman"
puts "Press enter to continue"
gets

while game

end
