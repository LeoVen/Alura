# conda create -n MachineLearning python=2.7 scikit-learn pandas

# 1 - Red
# 2 - Green
# 3 - Blue

from sklearn.naive_bayes import MultinomialNB

def main():
	g1 = [39, 252, 20]
	g2 = [26, 196, 11]
	g3 = [68, 242, 53]
	g4 = [20, 255, 0]
	g5 = [43, 198, 29]

	r1 = [255, 0, 0]
	r2 = [201, 20, 20]
	r3 = [249, 20, 37]
	r4 = [206, 22, 22]
	r5 = [216, 35, 19]

	b1 = [69, 20, 249]
	b2 = [30, 5, 193]
	b3 = [51, 23, 234]
	b4 = [0, 25, 255]
	b5 = [20, 37, 188]

	data = [g1, g2, g3, g4, g5, r1, r2, r3, r4, r5, b1, b2, b3, b4, b5]

	marks = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]

	model = MultinomialNB()

	model.fit(data, marks)

	# 1, 2, 3, 2, 3, 3, 1, 3, 1, 1
	guess = [[211, 8, 32], [45, 226, 18], [35, 52, 206], [43, 140, 2], [29, 77, 140],
			[0, 34, 79], [214, 0, 60], [35, 126, 175], [175, 34, 74], [221, 33, 0]]


	result = model.predict(guess)

	print(result)


if __name__ == '__main__':
	main()