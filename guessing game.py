# guessing game 
from random import randint
from sys import exit

x = randint(1,100)
#print (x)



guesses = [0]
print('The given number is between 1 and 100. \nTry to guess the number in 10 guesses')
#guess = int(input('first guess: '))
#if guess == x:
#    print('Correct! you have guessed in the very first attempt!')
#else:
while True:
    guess = int(input('Guess the number: '))
    guesses.append(guess)
    if guess == x:
        print('Correct! You have guessed in {} guesses' .format(len(guesses)-1))
        break
    elif abs(guess-x)>10:
        print('Absolute difference between the guess and the number is more than 10')
        continue
    elif abs(guess-x)<10:
        print('Absolute difference between the guess and the number is less than 10')
        break
while True:
    guess = int(input('Next guess: '))
    guesses.append(guess)    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Guess in the range of 1 and 100')
        continue
    elif guess == x:
        print('Correct! You have guessed in {} guesses' .format(len(guesses)-1))
        break
    if guesses[-2]:
        if abs(guesses[-2] - x) > abs(guess - x):
            print('Current guess is closer to the number than previous guess in absolute terms')
        else:
            print('Previous guess is closer to the number in absolute terms')
    else:
        if abs(guess-x)<=10:
            print('Absolute difference between the guess and the number is less than or equal to 10')
        else:
            print('Absolute difference between the guess and the number is more than 10')

    if len(guesses) > 10:
        print( '\n You have reached the number of guesses limit. \n The answer is {}'  .format(x))
        break
