import random
from HangmanLib import HANGMAN_PICS
from HangmanLib import WORDS


def getRandomWord(wordList):
    return random.choice(wordList)
def displayBoard(HANGMAN_PICS,missedLetters,correctLetters,secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed Letters: ",end="")
    for letter in missedLetters:
        print(letter,end="")
    print()
    blanks="_"*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
    for letter in blanks:
        print(letter,end="")
    print()

def getGuess(alreadyGuessed):
    while True:
        print("guess a letter")
        guess=input().lower()
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess in alreadyGuessed:
            print("you have already guessed ")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("please enter a letter")
        else:
            return guess
            
def playAgain():
    print("do you wanna play again (yes or no)?")
    return input().lower().startswith("y")

def playGame():
    missedLetters=""
    correctLetters=""
    secretWord=getRandomWord(WORDS)
    gameIsDone=False
    print("H A N G M A N")
    while True:
        displayBoard(HANGMAN_PICS,missedLetters,correctLetters,secretWord)
        guess=getGuess(missedLetters+correctLetters)
        if guess in secretWord:
            correctLetters+=guess
            foundAllLetters=True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters=False
                    break
            if foundAllLetters:
                print("yes! the secret word is "+secretWord+"\nYou have won!!")
                gameIsDone=True
        else:
            missedLetters+=guess
            if len(missedLetters)==len(HANGMAN_PICS)-1:
                displayBoard(HANGMAN_PICS,missedLetters,correctLetters,secretWord)
                print("you have run out of guess!\n after "+str(len(missedLetters))+" missed guesses and "+str(len(correctLetters))+" correct guess, the word was "+secretWord)
                gameIsDone=True
        if gameIsDone:
            if playAgain():
                missedLetters=""
                correctLetters=""
                secretWord=getRandomWord(WORDS)
                gameIsDone=False
            else:
                break
playGame()