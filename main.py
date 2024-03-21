import sys
from PyQt5.QtWidgets import QApplication
import MenuInterface


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuInterface.MainWindow()
    window.show()
    sys.exit(app.exec_())