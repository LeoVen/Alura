# conda create -n MachineLearning python=2.7 scikit-learn pandas

import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from collections import Counter
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier


def fit_and_predict(model, X_train, Y_train, X_tests, Y_tests):

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

	print "\n{0} Machine Learning Algorithm".format(model.__class__.__name__)
	print "Hit rate: " + str(rate) + "%"
	print "Tested cases: " + str(len(X_tests))

	return rate

def main():
	data = pd.read_csv('data/clas.csv')

	# These are dataframes
	X_df = data[['recencia', 'frequencia', 'semanas_de_inscricao']]
	Y_df = data['situacao']

	# Getting dummies (changing attributes to separated columns of 1 and 0)
	X_dummies_df = pd.get_dummies(X_df)
	Y_dummies_df = Y_df

	# Extracting values from dataframe making an array
	X = X_dummies_df.values
	Y = Y_dummies_df.values

	# 80% of data for training
	# 10% of data for tests
	# 10% of data for real cases
	p = 0.8
	pt = 0.1

	l = len(X)

	X_train = X[:int(l * p)]
	Y_train = Y[:int(l * p)]

	X_tests = X[int(l * p) : int(l * (p + pt))]
	Y_tests = Y[int(l * p) : int(l * (p + pt))]

	X_eval = X[int((l * (p + pt))):]
	Y_eval = Y[int((l * (p + pt))):]

	# -------------------------------------------------- #
	# The efficiency of a simplified algorithm
	rate = 100.0 * max(Counter(Y_tests).itervalues()) / len(Y_tests)
	print "Hit rate of a simple algorithm : " + str(rate) + "%"
	# -------------------------------------------------- #

	mnb_model = MultinomialNB()

	ada_model = AdaBoostClassifier()

	ovr_model = OneVsRestClassifier(LinearSVC(random_state = 0))

	ovo_model = OneVsOneClassifier(LinearSVC(random_state = 0))

	mnb_rate = fit_and_predict(mnb_model, X_train, Y_train, X_tests, Y_tests)

	ada_rate = fit_and_predict(ada_model, X_train, Y_train, X_tests, Y_tests)

	ovr_rate = fit_and_predict(ovr_model, X_train, Y_train, X_tests, Y_tests)

	ovo_rate = fit_and_predict(ovo_model, X_train, Y_train, X_tests, Y_tests)

	results = {}

	results[mnb_rate] = mnb_model
	results[ada_rate] = ada_model
	results[ovr_rate] = ovr_model
	results[ovo_rate] = ovo_model

	# Set winning model
	winner = results[max(results)]

	# Final test with winning model
	# Predicting
	result = winner.predict(X_eval)

	# Checking the difference
	diff = (result == Y_eval)
	correct_Y = [d for d in diff if d]

	total_correct = len(correct_Y)
	total_elements = len(X_eval)

	# Hit rate
	rate = 100.0 * total_correct / total_elements

	print "\n!! Final Test for Winning Algorithm !!"
	print "{0} Machine Learning Algorithm".format(winner.__class__.__name__)
	print "Hit rate: " + str(rate) + "%"
	print "Tested cases: " + str(len(X_eval))


if __name__ == '__main__':
	main()

