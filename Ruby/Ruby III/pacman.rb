# #
# pacman.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 27/08/2018
#
# #

require_relative 'ui'

def read_map(number)
    file = "map#{number}.txt"
    text = File.read(file)
    return text.split("\n")
end

def find_player(map)
    ch = "H"
    map.each_with_index do |current_row, row|
        col = current_row.index ch
        if col
            return [row, col]
        end
    end
end

def calculate_position(hero, direction)
    hero = hero.dup

    mov = {
        "W" => [-1,  0],
        "S" => [+1,  0],
        "A" => [ 0, -1],
        "D" => [ 0, +1]
    }

    moves = mov[direction]

    if moves
        hero[0] += moves[0]
        hero[1] += moves[1]
    end

    return hero
end

def is_valid_position?(map, position)
    if position[0] < 0 || position[0] >= map.size
        return false
    end
    if position[1] < 0 || position[1] >= map[0].size
        return false
    end

    invalid = %w(X F)

    if invalid.include? map[position[0]][position[1]]
        return false
    end

    return true
end

def move_ghost(map, row, col)
    pos = [row, col + 1]
    if is_valid_position?(map, pos)
        map[row][col] = " "
        map[pos[0]][pos[1]] = "F"
    end
end

def ghost_movement(map)
    ghost = "F"

    map.each_with_index do |current_row, row|
        current_row.chars.each_with_index do |character, col|
            if character == ghost
                move_ghost(map, row, col)
            end
        end
    end
end

def play
   text_map = read_map(2)

    while true
        write_map(text_map)
        direction = get_movement
        hero = find_player(text_map)

        new_hero = calculate_position(hero, direction)

        if is_valid_position?(text_map, new_hero)
            text_map[hero[0]][hero[1]] = " "
            text_map[new_hero[0]][new_hero[1]] = "H"
            ghost_movement text_map
        else
            next
        end

    end
end