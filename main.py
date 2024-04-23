from PySide6 import QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Основное окно')
        self.resize(300, 200)


app = QtWidgets.QApplication()

window = MainWindow()
pal = window.palette()
pal.setColor(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window, QtGui.QColor("#008800"))
pal.setColor(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, QtGui.QColor("#ff0000"))
window.setPalette(pal)
window.show()

app.exec()

