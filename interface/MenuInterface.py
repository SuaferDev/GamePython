from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QDialog, QComboBox
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt

from interface.RuleInterface import DialogRule
from interface.GameInterface import DialogGame
from logic import GameHelper


class DialogPlay(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки игры")
        self.setStyleSheet("background-color: #171628; color: #AFA8FF;")
        self.setGeometry(250, 250, 300, 300)
        self.selected_size = "6x6"
        self.selected_time = "1"

        font_id = QFontDatabase.addApplicationFont("interface/font/font_main.ttf")


        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family)
        else:
            font = self.font()

        layout = QVBoxLayout()

        labelSize = QLabel("Выберите размер поля и время игры")
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
        numbers = size.split("x")
        height = int(numbers[0])
        width = int(numbers[1])
        game = GameHelper.createGame(int(time) * 60, height, width)
        print("-1")
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

        font_id = QFontDatabase.addApplicationFont("interface/font/font_main.ttf")

        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            font_family = font_families[0]
            font = QFont(font_family)
        else:
            print("No font families found.")

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