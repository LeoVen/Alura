# #
# ui.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 27/08/2018
#
# #

def welcome
    puts "Welcome to Pac-Man"
    puts "Press enter to continue"
    gets
end

def write_map(map)
    puts map
end

def get_movement
    puts "Where to go now?"
    return gets.strip.upcase
end