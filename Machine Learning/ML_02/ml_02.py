# conda create -n MachineLearning python=2.7 scikit-learn pandas
# Using data/clas.csv

import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from collections import Counter
from sklearn.cross_validation import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier


def fit_and_predict(model, X_train, Y_train, kfold):

	# Training model with kfold
	scores = cross_val_score(model, X_train, Y_train, cv = kfold)

	result = np.mean(scores)

	print "\n{0} Machine Learning Algorithm".format(model.__class__.__name__)
	print "Hit rate: " + str(result * 100) + "%"
	print "Total tested: " + str(len(Y_train))
	print "Kfolds: " + str(kfold)
	print "Scores: "
	print scores

	return result * 100


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

	# 80% of data for training and testing
	# 20% of data for real cases
	t = 0.8

	l = len(X)

	X_train = X[:int(l * t)]
	Y_train = Y[:int(l * t)]

	X_eval = X[int(l * t):]
	Y_eval = Y[int(l * t):]

	# -------------------------------------------------- #
	# The efficiency of a simplified algorithm
	rate = 100.0 * max(Counter(Y_train).itervalues()) / len(Y_train)
	print "\nHit rate of a simple algorithm : " + str(rate) + "%"
	# -------------------------------------------------- #

	kfold = 10

	mnb_model = MultinomialNB()

	ada_model = AdaBoostClassifier()

	ovr_model = OneVsRestClassifier(LinearSVC(random_state = 0))

	ovo_model = OneVsOneClassifier(LinearSVC(random_state = 0))

	mnb_rate = fit_and_predict(mnb_model, X_train, Y_train, kfold)

	ada_rate = fit_and_predict(ada_model, X_train, Y_train, kfold)

	ovr_rate = fit_and_predict(ovr_model, X_train, Y_train, kfold)

	ovo_rate = fit_and_predict(ovo_model, X_train, Y_train, kfold)

	results = {}

	results[mnb_rate] = mnb_model
	results[ada_rate] = ada_model
	results[ovr_rate] = ovr_model
	results[ovo_rate] = ovo_model

	# Set winning model
	winner = results[max(results)]

	winner.fit(X_train, Y_train)

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

