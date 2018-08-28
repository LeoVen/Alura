# #
# array.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 21/08/2018
#
# #

# to array
array0 = ("1".."10").to_a

# Prints each element in one line
puts array0

# Prints array in one line
puts array0.join(' ')

# Array class
puts array0.class

array1 = (1..10).to_a

for x in 0..array1.size
	# Prints doesn't add newline character
	print array1[x].to_s + ' '
end

puts

sum = 0

for x in array1
	sum += x
end

puts "Sum: " + sum.to_s

# How many even numbers in array1
puts array1.count(&:even?)

# Add new element in the array
array1 << 11
array1 << 12

print array1
puts
# (position, value)
array1.insert(0, 0)
array1.insert(0, -1)
array1.insert(0, -2)

print array1

puts "\n\nLength of array0 is #{array0.length} and the length of array1 is #{array1.length}"

text = "  Lorem Ipsum Dolor Sit Amet, consectetur adipiscing elit. Suspendisse vulputate tellus vel suscipit tristique.  \n"
num = 12

puts num.even?
puts num.odd?
puts text.upcase
puts text.downcase
puts text.capitalize
puts text.strip # removes white spaces