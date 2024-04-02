import random
from logic.Game import Game
from logic.Tile import Tile

colorPool = ["#22223C", "#1D1D32", "#171729"]


'''
def createMap(height, width):
    board = [[random.randint(1, 6) for _ in range(height)] for _ in range(width)]
    return board
'''



def createGame(time, height, width):
    return Game(time, createMap(height, width))


def createMap(height, width):
    board = [[Tile(0, "") for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            board[i][j].setValue(random.randint(1, 6))
            board[i][j].setColor(generateColor())
    return board


def generateColor():
    randomIndex = random.randint(0, len(colorPool)-1)
    return colorPool[randomIndex]


'''
def createGame(time, size):
    numbers = size.split("x")
    height = int(numbers[0])
    width = int(numbers[1])
    return Game(int(time), createMap(height, width))
'''


