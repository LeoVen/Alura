import csv

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
