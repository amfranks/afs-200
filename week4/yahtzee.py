import random 

###################################################################

class Die:

    def __init__(self, numOfSides = 6): # Constructor function.
        self.numOfSides = numOfSides
        self.diceVal = 1

    def roll(self): # Rolls the dice.
        self.diceVal = random.randint(1, self.numOfSides) 

    def getCurrentFaceValue(self): # Get's the dices current value.
        return self.diceVal

    def showDieFace(self): # Display dices current value.
        print(f"({self.diceVal})")

###################################################################

def rollFiveDice(numOfSidesArray): # Rolls 5 different dice.

    yahtzee = True
    dicePreviousValue = None

    arrayOfValues = [] # This array will store all 5 dice values.

    myDice = [Die(), Die(), Die(), Die(), Die()]

    for die in myDice:
        die.roll()
        die.showDieFace()

    for x in range(1, len(myDice)):
        if myDice[0].getCurrentFaceValue() != myDice[x].getCurrentFaceValue():
            yahtzee = False
            break

    if yahtzee == True:
        print("\n YAHTZEE")               

rollFiveDice([6, 6, 6, 6, 6]) # Enter a value to signify a number of sides for each dice.