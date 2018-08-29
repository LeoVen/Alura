# #
# ui.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 28/08/2018
#
# #

def welcome
	puts "Welcome to Pacman"
	puts "Press enter to continue"
	gets
end

def get_movement
	puts "Where to go now?"
	return gets.strip.upcase
end

def write_map(map)
	puts map
end

def game_over
	puts "\n\n\n\n"
	puts "Game Over"
end