import random
secretNumber = random.randint(1,11)
print('I am thinking of a number between 1 and 10')

#6 guess
for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope! The number I was thinking of was ' + str(secretNumber))
