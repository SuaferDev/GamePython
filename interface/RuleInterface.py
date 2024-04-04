from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class DialogRule(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Правила")
        self.setStyleSheet("background-color: #171628; color: #AFA8FF;")
        self.setGeometry(250, 250, 300, 300)

        layout = QVBoxLayout()

        font_id = QFontDatabase.addApplicationFont("interface/font/font_main.ttf")

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