import random, sys
print('Rock, Paper, Scissors')

#keeping track of variables
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors (l)izard (sp)ock or (q)uit')
        playMove = input()
        if playMove == 'q':
            sys.exit() # quit the program
        if playMove == 'r' or playMove == 'p' or playMove == 's' or playMove == 'l' or playMove == 'sp':
            break
        print('Type one of r, p, s, l, sp or q.')

    if playMove == 'r':
        print('Rock versus...')
    elif playMove == 'p':
        print('Paper versus...')
    elif playMove == 's':
        print('Scissors versus...')
    elif playMove == 'l':
        print('Lizard versus...')
    elif playMove == 'sp':
        print('Spock versus...')

    randomeNumber = random.randint(1,5)
    if randomeNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomeNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomeNumber == 3:
        computerMove = 's'
        print('Scissors')
    elif randomeNumber == 4:
        computerMove == 'l'
        print('Lizard')
    elif randomeNumber == 5:
        computerMove == 'sp'
        print('Spock')

    if playMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playMove == 'r' and computerMove == 's':# Rock crushes Scissors
        print('You Win!')
        wins = wins + 1
    elif playMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
    elif playMove == 's' and computerMove == 'p':# Scissors cut paper (done)
        print('You Win!')
        wins = wins + 1
    elif playMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'p' and computerMove == 'r':# Ppaer covers Rock (done)
        print('You Win!')
        wins = wins + 1
    elif playMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'r' and computerMove == 'l':# Rock crushes Lizard (done)
        print('You win!')
        wins = wins + 1
    elif playMove == 'l' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'l' and computerMove == 'sp':# Lizard poisons Spock (done)
        print('You win!')
        wins = wins + 1
    elif playMove == 'sp' and computerMove == 'l':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'sp' and computerMove == 's':# Spock smashes Scissors (done)
        print('You win!')
        wins = wins + 1
    elif playMove == 's' and computerMove == 'sp':
        print('You lose!')
        losses = losses + 1
    elif playMove == 's' and computerMove == 'l': #Scissors decapitate Lizard (done)
        print('You win!')
        wins = wins + 1
    elif playMove == 'l' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'l' and computerMove == 'p': #Lizard eats paper
        print('You win!')
        wins = wins + 1
    elif playMove == 'p' and computerMove == 'l':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'p' and computerMove == 'sp': # Paper disproves Spock
        print('You win!')
        wins = wins + 1
    elif playMove == 'sp' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playMove == 'sp' and computerMove == 'r': # Spock vaporizes Rock
        print('You win!')
        wins = wins + 1
    elif playMove == 'r' and computerMove == 'sp':
        print('You lose!')
        losses = losses + 1
