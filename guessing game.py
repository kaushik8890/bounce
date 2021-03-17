# guessing game 
from random import randint
x = randint(1,100)
#print (x)

guesses = [0]
while True:
    guess = int(input('What is your guess? '))
    guesses.append(guess)    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Guess in the range of 1 and 100')
        continue
    elif guess == x:
        print('Correct! You have guessed in {} guesses' .format(len(guesses)-1))
        break
    if guesses[-2]:
        if abs(guesses[-2] - x) > abs(guess - x):
            print('Current guess is closer to the number in absolute terms')
        else:
            print('Previous guess is closer to the number in absolute terms')
    else:
        if abs(guess-x)<=10:
            print('Absolute difference between the guess and the number is less than or equal to 10')
        else:
            print('Absolute difference between the guess and the number is more than 10')

