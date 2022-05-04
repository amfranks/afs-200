secretWord = "PROFESSOR"
lettersGuessed = []
wordBoard = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
isFound = False
guessesLeft = 5

##########################################################################

def showBoard():
        word = ""
        for i in wordBoard:
            word += (i + " ")
        print (word)

def checkGuess(letterGuessed):
        letterFound = False

        for i in range(0, len(secretWord)): # Loop through secretWord.
            if secretWord[i] == letterGuessed:
                letterFound = True
                lettersGuessed.append(secretWord[i])
                wordBoard[i] = letterGuessed      
            else:
                lettersGuessed.append(letterGuessed)
        return letterFound

##########################################################################

while isFound == False and guessesLeft > 0: 
    print("\nCan you guess the secret occupation?\n")
    letterGuessed = input("Guess a letter: ").upper()

    isGuessed = False

    for i in lettersGuessed:
            if i == letterGuessed: 
                isGuessed = True

    if isGuessed == False:
        if checkGuess(letterGuessed) == True:
            showBoard()

            underScoresLeft = len(wordBoard)

            for i in wordBoard:
                if i != "_":
                    underScoresLeft -= 1
                
            if underScoresLeft == 0:
                print("You guessed right! Game over!")
                isFound = True

        else:
            guessesLeft -= 1
            print(f"Sorry, wrong guess. You have {guessesLeft} guesses left.")

        if guessesLeft == 0:
            print("Out of guesses. Game over!")
            print("The secret word was: " + secretWord)
            break
    else: 
        print("Please try again.")
        print(letterGuessed + " is already guessed!")