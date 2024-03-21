import GameHelper

field = [[3, 1, 5, 3],
        [1, 1, 2, 3],
        [3, 4, 2, 4],
        [6, 3, 3, 5]]

def printGame():
    for i in range(len(game.getField())):
            print(game.getField()[i])


game = GameHelper.createGame(10,"4x4")
game.setField(field)
printGame()

for i in range(len(game.getC())):
    print(game.test1(i)," ", end="")


game.click(0,0)
game.click(1,2)
print()
for i in range(len(game.getC())):
    print(game.test1(i)," ", end="")
game.click(1,0)
for i in range(len(game.getC())):
    print(game.test1(i)," ", end="")
game.click(1,2)
print()
for i in range(len(game.getC())):
    print(game.test1(i)," ", end="")
game.click(2,1)



print()
printGame()
print(game.getScore())

















