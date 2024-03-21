from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QDialog, QComboBox, QTableWidget, \
    QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QColor
import GameHelper


class DialogRule(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Правила")
        self.setStyleSheet("background-color: #171628; color: #AFA8FF;")
        self.setGeometry(250, 250, 300, 300)

        layout = QVBoxLayout()

        font_id = QFontDatabase.addApplicationFont("font/font_main.ttf")

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
        else:
            font = self.font()

        labelRule = QLabel("Нажимайте на элементы на поле для выбора,\nзначения с полей суммируются.\nЕсли сумма равна 10 выбранные поля пропадут,\nна их месте появтся новые и\nВы получите очки")
        labelRule.setAlignment(Qt.AlignCenter)
        labelRule.setFont(font)
        labelRule.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )
        layout.addWidget(labelRule)

        self.setLayout(layout)


class DialogPlay(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки игры")
        self.setStyleSheet("background-color: #171628; color: #AFA8FF;")
        self.setGeometry(250, 250, 300, 300)

        font_id = QFontDatabase.addApplicationFont("font/font_main.ttf")

        self.selected_size = "6x6"
        self.selected_time = "1"

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
        else:
            font = self.font()

        layout = QVBoxLayout()

        labelSize = QLabel("Выберите размер поля и время игры:")
        labelSize.setAlignment(Qt.AlignCenter)
        labelSize.setFont(font)
        labelSize.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )
        layout.addWidget(labelSize)

        size_label = QLabel("Размер поля:")
        size_label.setFont(font)
        size_label.setStyleSheet("color: white; font-size: 30px;")
        self.size_combo = QComboBox()
        self.size_combo.addItem("6x6")
        self.size_combo.addItem("10x10")
        self.size_combo.addItem("15x15")
        self.size_combo.addItem("20x20")
        self.size_combo.setFont(font)
        self.size_combo.setStyleSheet("color: white; font-size: 30px;")
        layout.addWidget(size_label)
        layout.addWidget(self.size_combo)

        labelTime = QLabel("Время игры (мин):")
        labelTime.setFont(font)
        labelTime.setStyleSheet("color: white; font-size: 30px; margin-top: 40px;")
        self.time_combo = QComboBox()
        self.time_combo.addItem("1")
        self.time_combo.addItem("5")
        self.time_combo.addItem("10")
        self.time_combo.setFont(font)
        self.time_combo.setStyleSheet("color: white; font-size: 30px;")
        layout.addWidget(labelTime)
        layout.addWidget(self.time_combo)

        self.size_combo.currentIndexChanged.connect(self.size_changed)
        self.time_combo.currentIndexChanged.connect(self.time_changed)

        buttonOk = QPushButton("OK")
        buttonOk.setFont(font)
        buttonOk.setStyleSheet("color: #FFC500; font-size: 30px; margin-top: 40px; border: 2px solid #302F42; border-radius: 10px;")
        buttonOk.clicked.connect(lambda: self.play(self.selected_size, self.selected_time))
        layout.addWidget(buttonOk)

        self.setLayout(layout)

    def play(self, size, time):
        game = GameHelper.createGame(int(time)*60, size)
        self.accept()
        dialog = DialogGame(game)
        dialog.exec_()


    def size_changed(self): self.selected_size = self.size_combo.currentText()

    def time_changed(self): self.selected_time = self.time_combo.currentText()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #171628;")
        self.setGeometry(100, 100, 700, 700)
        main_layout = QVBoxLayout()

        font_id = QFontDatabase.addApplicationFont("font/font_main.ttf")

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
        else:
            font = self.font()

        label = QLabel("Блиц\nСложение")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)
        label.setStyleSheet("color: #AFA8FF; font-size: 100px;")
        main_layout.addWidget(label, alignment=Qt.AlignCenter)

        button_layout = QHBoxLayout()

        buttonPlay = QPushButton("Играть")
        buttonRule = QPushButton("Правила")
        buttonExit = QPushButton("Выйти")

        buttonPlay.setFont(font)
        buttonRule.setFont(font)
        buttonExit.setFont(font)

        buttonPlay.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )
        buttonRule.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )
        buttonExit.setStyleSheet(
            "color: white; font-size: 30px;"
            "QPushButton { background-color: transparent; border: 2px solid white; border-radius: 10px; }"
            "QPushButton:hover { background-color: yellow; }"
        )

        buttonPlay.clicked.connect(self.createDialogPlay)
        buttonRule.clicked.connect(self.createDialogRule)
        buttonExit.clicked.connect(self.close)

        button_layout.addWidget(buttonPlay)
        button_layout.addWidget(buttonRule)
        button_layout.addWidget(buttonExit)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("Блитц Сложение")

    def createDialogPlay(self):
        dialog = DialogPlay(self)
        dialog.exec_()


    def createDialogRule(self):
        dialog = DialogRule(self)
        dialog.exec_()


class DialogGame(QDialog):
    def __init__(self, game, parent=None):
        super().__init__(parent)
        self.setWindowTitle("БЛИТЦ-СЛОЖЕНИЕ")
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
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setFocusPolicy(Qt.NoFocus)

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
            self.accept()
            dialog = DialogEndGame(self.game)
            dialog.exec_()

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

        labelTitle = QLabel("Игра окончена время вышло")
        labelTitle.setFont(font)
        labelTitle.setAlignment(Qt.AlignCenter)
        labelResult = QLabel("Вы набрали " + str(game.getScore()) + " очков")
        labelResult.setFont(font)
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
        s = str(self.game.getSize())+"x"+str(self.game.getSize())
        game = GameHelper.createGame(1 * 60, s)
        self.close()
        dialog = DialogGame(game)
        dialog.exec_()
    def toMenu(self):
        window = MainWindow()
        window.show()
        self.close()