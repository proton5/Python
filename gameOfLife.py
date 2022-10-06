# If a living square has two or three living neighbors, it continues to live on the next step.
# If a dead square has exactly three living neighbors, it comes alive on the next step
# Every other square dies or remains dead on the next step.
import time,random,copy
from turtle import right
def createBoard(nextCells):
    for x in range(WIDTH):
        column = []
        for y in range(HEIGHT):
            if random.randint(0,1) == 0:
                column.append('X')
            else:
                column.append(' ')
        nextCells.append(column)
def printCurrentBoard(currentCells):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='')
        print()
def proceed(currentCells):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Mod makes sure its between 0 and one less than the width
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            #check living neighbors
            numNeighbors = 0
            #check top left neighbor
            if currentCells[leftCoord][aboveCoord] == 'X':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == 'X':
                 numNeighbors += 1
            #check top right neighbor
            if currentCells[rightCoord][aboveCoord] == 'X':
                numNeighbors += 1
            #check left neighbor
            if currentCells[leftCoord][y] == 'X':
                 numNeighbors += 1
            #check right neighbor
            if currentCells[rightCoord][y] == 'X':
                numNeighbors += 1
            #check bottom left neighbor
            if currentCells[leftCoord][belowCoord] == 'X':
                numNeighbors += 1
            if currentCells[x][belowCoord] == 'X':
                numNeighbors += 1
            #check bottom right neighbor
            if currentCells[rightCoord][belowCoord] == 'X':
                numNeighbors += 1
            # set cells based on rules
            if currentCells[x][y] == 'X' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = 'X'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = 'X'
            else:
                nextCells[x][y] = ' '
# Main entry point
WIDTH = 60
HEIGHT = 20
nextCells = []
createBoard(nextCells)
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    printCurrentBoard(currentCells)
    proceed(currentCells)
    time.sleep(1)
