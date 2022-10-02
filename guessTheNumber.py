import random
myNumber = random.randint(1,20)
print('Im thinking of a number between 1 and 20.')
print('You will get 6 guesses')
for guessesTaken in range(1,7) :
    print('What is your guess?')
    currentGuess = int(input())
    if currentGuess > myNumber :
        print('That is too high')
    elif currentGuess < myNumber :
        print('That guess is too low')
    else : break
if currentGuess == myNumber :
    print('Correct! You guessed the right number! (' + str(myNumber) + ')' + ' You guessed it correctly in ' + str(guessesTaken) + ' guesses!') 
else : print('Sorry I was thinking of the number: ' + str(myNumber))