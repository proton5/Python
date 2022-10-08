import sys,random
tictactoeBoard = { "topLeft": " ", "topMiddle": " ", "topRight": " ",
                "leftMiddle": " ", "middle": " ", "rightMiddle": " ",
                "leftBottom": " ", "middleBottom": " ", "rightBottom": " "
}
def displayBoard():
    print(" ", end="")
    print(tictactoeBoard["topLeft"], end="")
    print("|", end="")
    print(tictactoeBoard["topMiddle"], end="")
    print("|", end="")
    print(tictactoeBoard["topRight"], end="")
    print(" ")
    print(" -+-+- ")
    #second row
    print(" ", end="")
    print(tictactoeBoard["leftMiddle"], end="")
    print("|", end="")
    print(tictactoeBoard["middle"], end="")
    print("|", end="")
    print(tictactoeBoard["rightMiddle"], end="")
    print(" ")
    print(" -+-+- ")
    #third row
    print(" ", end="")
    print(tictactoeBoard["leftBottom"], end="")
    print("|", end="")
    print(tictactoeBoard["middleBottom"], end="")
    print("|", end="")
    print(tictactoeBoard["rightBottom"], end="")
    print(" ")
def displayHelp():
    print(" ", end="")
    print("tl", end="")
    print("|", end="")
    print("tm", end="")
    print("|", end="")
    print("tr", end="")
    print(" ")
    print(" --+--+-- ")
    #second row
    print(" ", end="")
    print("lm", end="")
    print("|", end="")
    print("m", end="")
    print("|", end="")
    print("rm", end="")
    print(" ")
    print(" --+--+-- ")
    #third row
    print(" ", end="")
    print("lb", end="")
    print("|", end="")
    print("mb", end="")
    print("|", end="")
    print("rb", end="")
    print(" ")
def TakeATurn():
    print("Where would you like to place your piece? (need help? press h)")
    currentTurn = input()
    if (currentTurn == 'h'):
        displayHelp()
    elif (currentTurn == 'tl'):
        if (tictactoeBoard["topLeft"] == ' '):
            tictactoeBoard["topLeft"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'tm'):
        if (tictactoeBoard["topMiddle"] == ' '):
            tictactoeBoard["topMiddle"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'tr'):
        if (tictactoeBoard["topRight"] == ' '):
            tictactoeBoard["topRight"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'lm'):
        if (tictactoeBoard["leftMiddle"] == ' '):
            tictactoeBoard["leftMiddle"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'm'):
        if (tictactoeBoard["middle"] == ' '):
            tictactoeBoard["middle"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'rm'):
        if (tictactoeBoard["rightMiddle"] == ' '):
            tictactoeBoard["rightMiddle"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'lb'):
        if (tictactoeBoard["leftBottom"] == ' '):
            tictactoeBoard["leftBottom"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'mb'):
        if (tictactoeBoard["middleBottom"] == ' '):
            tictactoeBoard["middleBottom"] = 'X'
        else:
            print("Place already taken")
    elif (currentTurn == 'rb'):
        if (tictactoeBoard["rightBottom"] == ' '):
            tictactoeBoard["rightBottom"] = 'X'
        else:
            print("Place already taken")
def checkWinLose(currentCheck):
    if (tictactoeBoard["topLeft"] == currentCheck and tictactoeBoard["topMiddle"] == currentCheck and tictactoeBoard["topRight"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["leftMiddle"] == currentCheck and tictactoeBoard["middle"] == currentCheck and tictactoeBoard["rightMiddle"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["leftBottom"] == currentCheck and tictactoeBoard["middleBottom"] == currentCheck and tictactoeBoard["rightBottom"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["topLeft"] == currentCheck and tictactoeBoard["leftMiddle"] == currentCheck and tictactoeBoard["leftBottom"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["topMiddle"] == currentCheck and tictactoeBoard["middle"] == currentCheck and tictactoeBoard["middleBottom"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["topRight"] == currentCheck and tictactoeBoard["rightMiddle"] == currentCheck and tictactoeBoard["rightBottom"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["topLeft"] == currentCheck and tictactoeBoard["middle"] == currentCheck and tictactoeBoard["rightBottom"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
    if (tictactoeBoard["topRight"] == currentCheck and tictactoeBoard["middle"] == currentCheck and tictactoeBoard["leftBottom"] == currentCheck):
        print('Player wins.') if currentCheck == 'X' else print("computer wins.")
        promptNewGame()
def promptNewGame():
    print("Play again? (y)es,(n)o")
    currentTurn = input()
    if (currentTurn == 'n'):
        sys.exit()
def computerTakesTurn():
    computerChooses = random.randint(1,9)
    if (computerChooses == 0):
        if (tictactoeBoard["topLeft"] == ' '):
            tictactoeBoard["topLeft"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 1):
        if (tictactoeBoard["topMiddle"] == ' '):
            tictactoeBoard["topMiddle"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 2):
        if (tictactoeBoard["topRight"] == ' '):
            tictactoeBoard["topRight"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 3):
        if (tictactoeBoard["leftMiddle"] == ' '):
            tictactoeBoard["leftMiddle"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 4):
        if (tictactoeBoard["middle"] == ' '):
            tictactoeBoard["middle"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 5):
        if (tictactoeBoard["rightMiddle"] == ' '):
            tictactoeBoard["rightMiddle"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 6):
        if (tictactoeBoard["leftBottom"] == ' '):
            tictactoeBoard["leftBottom"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 7):
        if (tictactoeBoard["middleBottom"] == ' '):
            tictactoeBoard["middleBottom"] = "O"
        else:
            computerTakesTurn()
    if (computerChooses == 8):
        if (tictactoeBoard["rightBottom"] == ' '):
            tictactoeBoard["rightBottom"] = "O"
        else:
            computerTakesTurn()
#game loop
while True:
    print()
    displayBoard()
    checkWinLose('X')
    TakeATurn()
    computerTakesTurn()
    checkWinLose('O')
