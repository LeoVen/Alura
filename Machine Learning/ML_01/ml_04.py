# conda create -n MachineLearning python=2.7 scikit-learn pandas
# using busca_02.csv

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from collections import Counter


def main():
	data = pd.read_csv('data/busca_02.csv')

	# These are dataframes
	X_df = data[['home', 'busca', 'logado']]
	Y_df = data['comprou']

	# Getting dummies (changing attributes to separated columns of 1 and 0)
	X_dummies_df = pd.get_dummies(X_df)
	Y_dummies_df = Y_df

	# Extracting values from dataframe making an array
	X = X_dummies_df.values
	Y = Y_dummies_df.values

	# 90% of data for training
	# 10% of data for tests
	p = 0.9

	train_size = int( p * len(Y) )
	test_size = len(Y) - train_size

	X_train = X[:train_size]
	Y_train = Y[:train_size]

	X_tests = X[-test_size:]
	Y_tests = Y[-test_size:]

	# -------------------------------------------------- #
	# The efficiency of a simplified algorithm
	rate = 100.0 * max(Counter(Y_tests).itervalues()) / len(Y_tests)
	print "Hit rate of a simple algorithm : " + str(rate) + "%"
	# -------------------------------------------------- #

	model = MultinomialNB()

	# Training model
	model.fit(X_train, Y_train)

	# Predicting
	result = model.predict(X_tests)

	# Checking the difference
	diff = (result == Y_tests)
	correct_Y = [d for d in diff if d]

	total_correct = len(correct_Y)
	total_elements = len(X_tests)

	# Hit rate
	rate = 100.0 * total_correct / total_elements

	print "\nMachine Learning Algorithm"
	print "Hit rate: " + str(rate) + "%"
	print "Tested cases: " + str(len(X_tests))


if __name__ == '__main__':
	main()