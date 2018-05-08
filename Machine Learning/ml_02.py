# conda create -n MachineLearning python=2.7 scikit-learn pandas
# Using acesso.csv

import csv
from sklearn.naive_bayes import MultinomialNB

def load_data():

	X = []
	Y = []

	file = open('data/acesso.csv', 'rb')

	reader = csv.reader(file)

	reader.next()

	for df_1, df_2, df_3, df_4 in reader:
		X.append([int(df_1), int(df_2), int(df_3)])
		Y.append(int(df_4))

	return X, Y

def main():
	X, Y = load_data()

	# 80% of data for training
	X_train = X[:80]
	Y_train = Y[:80]

	# 20% of data for tests
	X_tests = X[-20:]
	Y_tests = Y[-20:]

	model = MultinomialNB()

	# Training model
	model.fit(X_train, Y_train)

	# Predicting
	result = model.predict(X_tests)

	# Checking the difference
	diff = result - Y_tests
	correct_Y = [d for d in diff if d == 0]

	total_correct = len(correct_Y)
	total_elements = len(X_tests)

	# Hit rate
	rate = 100.0 * total_correct / total_elements

	print "Hit rate: " + str(rate) + "%"
	print "Tested cases: " + str(len(X_tests))


if __name__ == '__main__':
	main()