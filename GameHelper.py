import random
from Game import Game


def createMap(height, width):
    board = [[random.randint(1, 6) for _ in range(height)] for _ in range(width)]
    return board


def createGame(time, size):
    numbers = size.split("x")
    height = int(numbers[0])
    width = int(numbers[1])
    return Game(int(time), createMap(height, width))

