# #
# hero.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 28/08/2018
#
# #

class Hero
	
	attr_accessor :row, :column
	
	def new_position(direction)
		hero = self.dup
		
		movimentos = {
			"W" => [-1, 0],
			"S" => [+1, 0],
			"A" => [0, -1],
			"D" => [0, +1]
			}
		
			movimento = movimentos[direction]
		
		hero.row += movimento[0]
		hero.column += movimento[1]
		
		return hero
	end

	def direita
		new_position "D"
	end

	def cima
		new_position "W"
	end

	def esquerda
		new_position "A"
	end
	
	def baixo
		new_position "S"
	end

	def to_array
		[row, column]
	end

	def remove_from(map)
		map[row][column] = " "
	end

	def place_on(map)
		map[row][column] = "H"
	end

end