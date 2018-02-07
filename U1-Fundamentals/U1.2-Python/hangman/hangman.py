word = input("Type a word for someone to guess: ")
guesses = []
numfails = 0
maxfails = 7
completedword = []

for letter in word:
	completedword.append("_");

done = False

while not done:
	print("-----------------------------------")
	print("Lives Left: ", maxfails - numfails)
	print("Guesses So Far: ", guesses)
	print("Current Word: ", completedword)

	guess = input("Guess a letter: ")
	if(len(guess) > 1):
		print("That's too long!")
	elif(guess.isalpha() == False):
		print("That's not a letter!")
	elif(guess in guesses):
		print("You already guessed that!")
	else:
		guesses.append(guess)

		if(guess in word):
			print("you got a letter!")
			for idx in range(0, len(word)):
				if word[idx] == guess:
					completedword[idx] = guess

			done = True
			for idx in range(0, len(completedword)):
				if completedword[idx] == "_":
					done = False
					break
			if done:
				print("You won!")
		else:
			print("wrong guess!")
			numfails += 1

			if numfails >= maxfails:
				print("You lost!")
				done = True



