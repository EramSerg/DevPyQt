import sys

from PySide6 import QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.login = QtWidgets.QLabel('login')
        self.passwd = QtWidgets.QLabel('password')
        self.button = QtWidgets.QPushButton('Войти')


app = Window()
window = QtWidgets.QWidget()
window.show()



