from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QTableWidget, QLabel, QPushButton, QDialog, QHBoxLayout, QVBoxLayout, QTableWidgetItem
from PyQt5.QtCore import Qt

import GameHelper


class DialogGame(QDialog):
    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Правила")
        self.setStyleSheet("background-color: #171628; color: #AFA8FF;")
        self.game = game
        self.table = QTableWidget()
        self.pixel = None
        self.setGeometry(250, 250, self.game.getSize()*110, self.game.getSize()*110)

        font_id = QFontDatabase.addApplicationFont("font/font_main.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.pixel = QFont(font_family)
        else: self.pixel = self.font()
        self.pixel.setPointSize(30)

        self.drawMap()
        self.labelScore = QLabel("Score: {}".format(self.game.getScore()))
        self.labelTime = QLabel()
        self.labelScore.setFont(self.pixel)
        self.labelTime.setFont(self.pixel)

        buttonUpdate = QPushButton()
        pixmap = QPixmap("image/update_image.jpg")
        icon = QIcon(pixmap)
        buttonUpdate.setIcon(icon)
        buttonUpdate.setIconSize(QSize(60, 60))

        self.getTime()
        buttonUpdate.clicked.connect(self.updateField)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.labelScore, alignment=Qt.AlignLeft)
        top_layout.addWidget(self.labelTime, alignment=Qt.AlignCenter)
        top_layout.addWidget(buttonUpdate, alignment=Qt.AlignRight)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.table.cellClicked.connect(self.cellClickedHandler)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time)
        self.timer.start(1000)

    def updateField(self):
        self.game.getField(GameHelper.createMap(self.game.getSize(), self.game.getSize()))
        self.drawMap()

    def time(self):
        self.game.second()
        self.getTime()
        if self.game.getTime() == 0:
            self.timer.stop()

    def getTime(self):
        minutes = self.game.getTime() // 60
        seconds = self.game.getTime() % 60
        self.labelTime.setText('{:02d}:{:02d}'.format(minutes, seconds))

    def drawMap(self):
        self.table.setRowCount(self.game.getSize())
        self.table.setColumnCount(self.game.getSize())
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

        for i in range(self.game.getSize()):
            for j in range(self.game.getSize()):
                item = QTableWidgetItem(str(self.game.getField()[i][j]))
                self.table.setColumnWidth(i, 100)
                self.table.setRowHeight(i, 100)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(self.pixel)

                if self.game.checkTile(i, j):
                    item.setBackground(QColor("#000000"))
                else:
                    if self.game.getField()[i][j] < 3: item.setBackground(QColor("#2B2A40"))

                    if self.game.getField()[i][j] > 4: item.setBackground(QColor("#0F0E1C"))

                for p in range(len(self.game.getC())):
                    if i == self.game.getC()[p].getX() and j == self.game.getC()[p].getY():
                        item.setBackground(QColor("#000000"))

                self.table.setItem(i, j, item)

    def cellClickedHandler(self, row, column):
        item = self.table.item(row, column)
        if item is not None:
            self.game.click(row, column)
            self.drawMap()
            print(self.game.getScore())
            self.labelScore.setText("Score: {}".format(self.game.getScore()))


class DialogEndGame(QDialog):
    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Игра окончена")
        self.setStyleSheet("background-color: #171628; color: #AFA8FF;")
        self.setGeometry(250, 250, 300, 300)
        self.game = game

        layout = QVBoxLayout()

        font_id = QFontDatabase.addApplicationFont("font/font_main.ttf")

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
        else:
            font = self.font()
            print("-")

        labelTitle = QLabel("Игра окончена время вышло");
        labelTitle.setFont(font);
        labelTitle.setAlignment(Qt.AlignCenter)
        labelResult = QLabel("Вы набрали " + str(game.getScore()) + " очков");
        labelResult.setFont(font);
        labelResult.setAlignment(Qt.AlignCenter)

        labelTitle.setStyleSheet("color: white; font-size: 30px;")
        labelResult.setStyleSheet("color: white; font-size: 30px;")

        layout.addWidget(labelTitle)
        layout.addWidget(labelResult)

        button_layout = QHBoxLayout()

        buttonNewGame = QPushButton("Новая игра")
        buttonToMenu = QPushButton("В меню")

        buttonNewGame.setFont(font)
        buttonToMenu.setFont(font)

        buttonNewGame.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )
        buttonToMenu.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )

        buttonNewGame.clicked.connect(self.newGame)
        buttonToMenu.clicked.connect(self.toMenu)

        button_layout.addWidget(buttonNewGame)
        button_layout.addWidget(buttonToMenu)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def newGame(self):

    def toMenu(self):
        window = MainWindow()
        window.show()
        self.close()