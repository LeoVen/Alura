

def play():

	print("+-----------------------------+")
	print("|         Jogo da forca       |")
	print("+-----------------------------+")

	secret = "Atemoya"
	secret = secret.upper()
	letras = ["_" for i in secret]

	print("\nDica:")
	print("\nUma fruta")

	enforcou = False
	acertou = False

	tentativas = 0
	max_tentativas = len(secret) + 2

	chutadas = []

	while (not enforcou and not acertou):

		chute = input("\nChute uma letra > ")
		chute = chute.replace(" ", "").upper()

		if len(chute) > 1:
			print("\nChute inválido. Tente novamente.")
			continue

		if chute in chutadas:
			print("\nVocê já tentou essa letra!")
			continue

		chutadas.append(chute)

		index = 0
		for letra in secret:

			if chute == letra:
				letras[index] = chute
			
			index += 1

		print("\nPalavra:")
		print(letras)

		print("\nChutes:")
		print(chutadas)

		if "_" not in letras:
			acertou = True
			continue

		tentativas += 1

		if tentativas >= max_tentativas:
			enforcou = True

		print("\nTentativas restantes: {}".format(max_tentativas - tentativas))

		print("\n+-----------------------------+\n")


	print("\n")

	if acertou:
		print("+-----------------------------+")
		print("|    Parabens você ganhou!    |")
		print("+-----------------------------+")
	else:
		print("+-----------------------------+")
		print("| Ah não! Você foi enforcado! |")
		print("+-----------------------------+")

if __name__ ==  "__main__":
	play()