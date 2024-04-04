class Tile:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def getValue(self): return self.value
    def getColor(self): return self.color

    def setValue(self, value): self.value = value

    def setColor(self, color): self.color = color

