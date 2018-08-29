# #
# pacman.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 28/08/2018
#
# #

require_relative 'ui'
require_relative 'hero'

def read_map(number)
	file = "map#{number}.txt"
	
	text = File.read(file)
	
	return text.split("\n")
end

def find_player(map)
	hero_char = "H"
	
	map.each_with_index do |current_row, row|
		col = current_row.index hero_char
		if col
			hero = Hero.new
			hero.row = row
			hero.column = col
			return hero
		end
	end
	
	return nil
end

def valid_position?(map, position)
	rows = map.size
	columns = map[0].size

	lim_row = position[0] < 0 || position[0] >= rows
	lim_col = position[1] < 0 || position[1] >= columns
	
	if lim_row || lim_col
		return false
	end

	if map[position[0]][position[1]] == "X" || map[position[0]][position[1]] == "F"
		return false
	end

	true
end

def vector_sum(vetor1, vetor2)
	[vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]
end

def valid_positions(map, new_map, position)
	positions = []
	
	movements = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
	
	movements.each do |movement|
		new_position = vector_sum(position, movement)
		if valid_position?(map, new_position) && valid_position?(new_map, new_position)
			positions << new_position
		end
	end
	
	return positions
end

def move_ghost(map, new_map, row, column)
	positions = valid_positions(map, new_map, [row, column])
	
	if positions.empty?
		return
	end

	random = rand positions.size
	
	position = positions[random]

	map[row][column] = " "
	
	new_map[position[0]][position[1]] = "F"
end

def move_ghosts(map)
	ghost = "F"

	new_map = map.join("\n").tr("F", " ").split("\n")

	map.each_with_index do |current_row, row|
		current_row.chars.each_with_index do |current_char, column|
			if current_char == ghost
				move_ghost(map, new_map, row, column)
			end
		end
	end
	
	return new_map
end

def player_lost?(map)
	find_player(map) == nil
end

def make_removal(map, position, squares)
	
	if map[position.row][position.column] == "X"
		return
	end
	
	map[position.row][position.column] = " "

	remove(map, position, squares - 1)
end

def remove(map, position, squares)

	if squares == 0
		return
	end

	make_removal(map, position.direita, squares)
	make_removal(map, position.esquerda, squares)
	make_removal(map, position.cima, squares)
	make_removal(map, position.baixo, squares)
end

def joga
	map = read_map 3
	while true
		write_map map
		direction = get_movement

		hero = find_player map
		
		new_position = hero.new_position direction
		
		if !valid_position? map, new_position.to_array
			next
		end

		hero.remove_from map
		
		if map[new_position.row][new_position.column] == "*"
			remove(map, new_position, 4)
		end
		
		new_position.place_on map

		map = move_ghosts map
		
		if player_lost?(map)
			game_over
			break
		end
	end
end

def start_game
	welcome
	joga
end