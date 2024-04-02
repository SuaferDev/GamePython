import random
from logic import GameHelper
from logic.Tile import Tile


class TileChoosen:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self): return self.__x
    def getY(self): return self.__y


class Game:

    def __init__(self, time, board):
        self.__score = 0
        self.__time = time
        self.__board = board
        self.__chooseFields = []



    def getScore(self): return self.__score
    def getTime(self): return self.__time
    def getField(self): return self.__board
    def getSize(self): return len(self.__board)
    def getC(self): return self.__chooseFields



    def second(self): self.__time = self.__time - 1



    def checkTile(self, x, y):
        for i in range(len(self.__chooseFields)):
            if x == self.__chooseFields[i].getX() and y == self.__chooseFields[i].getY():
                return True
        return False

    def checkChooseField(self, x, y):
        for i in range(len(self.__chooseFields)):
            if x == self.__chooseFields[i].getX() and y == self.__chooseFields[i].getY():
                self.__chooseFields.pop(i)
                return
        self.__chooseFields.append(TileChoosen(x, y))


    def __checkColor(self):
        color = self.__board[self.__chooseFields[0].getX()][self.__chooseFields[0].getY()].getColor()
        for i in range(1, len(self.__chooseFields)):
            if color != self.__board[self.__chooseFields[i].getX()][self.__chooseFields[i].getY()].getColor():
                return False
        return True


    def click(self, x, y):
        self.checkChooseField(x, y)

        if self.__checkSum():
            self.resetField()
            self.clearField()
            print(self.__checkColor())
            if self.__checkColor():
                self.__score += 10 * len(self.__chooseFields) * 5
            else:
                self.__score += 10 * len(self.__chooseFields)
            self.__chooseFields = []


    def __checkSum(self):
        sumValue = 0
        for i in range(len(self.__chooseFields)):
            sumValue = sumValue + self.__board[self.__chooseFields[i].getX()][self.__chooseFields[i].getY()].getValue()
        return sumValue == 10

    def resetField(self):
        for i in range(len(self.__chooseFields)):
            self.__board[self.__chooseFields[i].getX()][self.__chooseFields[i].getY()].setValue(0)

    def clearField(self):
        rows = len(self.__board)
        cols = len(self.__board[0])
        result = [[Tile(0, "") for _ in range(cols)] for _ in range(rows)]

        for j in range(cols):
            row_ptr = rows - 1
            for i in range(rows - 1, -1, -1):
                if self.__board[i][j].getValue() != 0:
                    result[row_ptr][j] = self.__board[i][j]
                    row_ptr -= 1

        self.__board = result

        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i][j].getValue() == 0:
                    self.__board[i][j] = Tile(random.randint(1, 6), GameHelper.generateColor())


'''
import random


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self): return self.x
    def getY(self): return self.y


class Game:
    def __init__(self, time, board):
        self.__score = 0
        self.__time = time
        self.__field = board
        self.__chooseFields = []

    def getScore(self): return self.__score
    def getTime(self): return self.__time
    def getField(self): return self.__field
    def getSize(self): return len(self.__field)
    def getC(self):return self.__chooseFields

    def setField(self, field): self.__field = field
    def addScore(self): self.__score = self.__score + 10
    def second(self): self.__time = self.__time - 1

    def checkTile(self, x, y):
        for i in range(len(self.__chooseFields)):
            if x == self.__chooseFields[i].getX() and y == self.__chooseFields[i].getY():
                return True
        return False

    def checkChooseField(self, x, y):
        for i in range(len(self.__chooseFields)):
            if x == self.__chooseFields[i].getX() and y == self.__chooseFields[i].getY():
                self.__chooseFields.pop(i)
                return
        self.__chooseFields.append(Tile(x, y))

    def click(self, x, y):
        self.checkChooseField(x,y)

        if self.__checkSum():
            self.resetField()
            self.clearField()
            self.__score += 10
            self.__chooseFields = []

    def __checkSum(self):
        sumValue = 0
        for i in range(len(self.__chooseFields)):
            sumValue = sumValue + self.__field[self.__chooseFields[i].getX()][self.__chooseFields[i].getY()]
        return sumValue == 10

    def resetField(self):
        for i in range(len(self.__chooseFields)):
            self.__field[self.__chooseFields[i].getX()][self.__chooseFields[i].getY()] = 0

    def clearField(self):
        rows = len(self.__field)
        cols = len(self.__field[0])
        result = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            row_ptr = rows - 1
            for i in range(rows - 1, -1, -1):
                if self.__field[i][j] != 0:
                    result[row_ptr][j] = self.__field[i][j]
                    row_ptr -= 1

        self.__field = result

        for i in range(len(self.__field)):
            for j in range(len(self.__field[i])):
                if self.__field[i][j] == 0: self.__field[i][j] = random.randint(1, 6)

'''
