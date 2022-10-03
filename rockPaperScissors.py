import random, sys
print('Rocky, Paper, Scissors')
wins = 0
losses = 0
ties = 0
while True:
   print(str(wins) + ' wins, ' + str(losses) + ' losses,' + str(ties) + ' ties')
   print('Enter your move: (r)ock, (s)cissors, (p)aper, or (q)uit')
   playerMove = input()
   if playerMove == 'q':
    sys.exit()
   # display what the player chose
   if playerMove == 'r':
      print('Rock vs...')
   elif playerMove == 'p':
      print('Paper vs...')
   elif playerMove == 's':
      print('Scissors vs...')
   # Computer chose
   cRandomNumber = random.randint(1,3)
   if cRandomNumber == 1:
      computerChoice = 'r'
      print('Rock')
   elif cRandomNumber == 2:
      computerChoice = 'p'
      print('Paper')
   elif cRandomNumber == 3:
      computerChoice = 's'
      print('Scissors')
   # record wins, losses, ties
   if playerMove == computerChoice:
      ties = ties + 1
   if playerMove == 'r' and computerChoice == 'p':
      losses = losses + 1
   if playerMove == 'r' and computerChoice == 's':
      wins = wins + 1
   if playerMove == 'p' and computerChoice == 'r':
      wins = wins + 1
   if playerMove == 'p' and computerChoice == 's':
      losses = losses + 1
   if playerMove == 's' and computerChoice == 'r':
      losses = losses + 1
   if playerMove == 's' and computerChoice == 'p':
      wins = wins + 1
   
   
   