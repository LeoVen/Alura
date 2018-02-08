import re

exp = r'(\d\d)(\w)'

target = '11a22b33c44d55e'

result = re.finditer(exp, target)

for i in result:
	print("{} | {} | {} | [{}, {}]".format(i.group(), i.group(1), i.group(2), i.start(), i.end()))


# Agora com data

print()
regex = '-'
replace = '/'
target = '2018-02-08'
print(target)
result = re.sub(regex, replace, target)
print(result)