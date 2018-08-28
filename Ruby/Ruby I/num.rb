# #
# num.rb
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 22/08/2018
#
# #

S = "2" # string
A = 2   # int
B = 2.1 # float

puts S.to_i # to int
puts S.to_f # to float
puts S.to_r # to rational
puts S.to_c # to complex

puts
Q = -4.0/3.0

puts Q
puts Q.to_r
puts Q.abs   # absolute value
puts Q.ceil
puts Q.floor

puts
puts "0xff".to_i(base=16)

puts
puts "11".to_i            # 11
puts "11".to_i(base=2)    # 3
puts "11".to_i(base=8)    # 9
puts "11".to_i(base=16)   # 17

puts

for x in 1..10 #[1, 10]
	# rand() = [0, 1)
	puts rand(200) # [0, 200)
end

puts

for x in 1..20

	puts rand(10..20) # [10, 20]
end


puts
num = 5     # 5
num += 1    # 6
num -= 2    # 4
num *= 2    # 8
num /= 4    # 2
num **= 10  # 1024
num %= 10   # 4

puts num

puts
puts 2 ** 10                # power
puts (16 ** (1.0/2.0)).to_i # root

n = 2 ** 32 - 1

puts "Binary : #{n.to_s(2)}"
puts "Octal  : #{n.to_s(8)}"
puts "Hex    : #{n.to_s(16)}"

puts
puts 12.5.to_s(base=2)