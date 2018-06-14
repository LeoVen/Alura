#! -*- coding: utf8 -*-
# conda create -n MachineLearning python=2.7 scikit-learn pandas nltk

import nltk
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


def text_array(text, translator, stemmer):
	
	array = [0] * len(translator)

	for word in text:
		if len(word) > 0:
			stem = stemmer.stem(word)
			if stem in translator:
				array[translator[stem]] += 1

	return array


def main():
	data = pd.read_csv('data/emails.csv', encoding="utf-8")

	emails = data['email']
	
	phrases = emails.str.lower()
	
	# nltk.download("punkt")
	texts = [nltk.tokenize.word_tokenize(tokens) for tokens in phrases]

	# nltk.download('stopwords')
	stopwords = nltk.corpus.stopwords.words("portuguese")

	# RSLP = Removedor de Sufixos da Lingua Portuguesa
	# nltk.download('rslp')
	stemmer = nltk.stem.RSLPStemmer()

	dictionary = set()

	for words in texts:
		# Removes empty words, small words and stopwords
		valid_words = [stemmer.stem(w) for w in words if w not in stopwords and len(w) > 2]
		dictionary.update(valid_words)

	dict_size = len(dictionary)

	temp_tuples = zip(dictionary, xrange(dict_size))

	translator = {word:index for word, index in temp_tuples}

	array_texts = [text_array(email, translator, stemmer) for email in texts]

	# Defining X and Y
	X = np.array(array_texts)
	Y = np.array(data['class'].tolist())

	# 80% of data for training and testing
	# 20% of data for real cases
	t = 0.8

	l = len(X)

	# Training data
	X_train = X[0:int(l * t)]
	Y_train = Y[0:int(l * t)]

	# 'Final exam' data
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
	
	print "\nTotal words used in dictionary: {0}".format(len(dictionary))


if __name__ == "__main__":
	main()