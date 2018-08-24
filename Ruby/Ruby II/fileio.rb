# #
# fileio.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 24/08/2018
#
# #

# Reads everything and closes
text = File.read("lorem_ipsum.txt")

print text.split("\n")

puts "\n\n\n"

# Open a file and have custom reading
file = File.new("lorem_ipsum.txt")

# Gets first line
print file.gets

file.close