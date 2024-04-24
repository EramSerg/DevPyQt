from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        vbox = QtWidgets.QVBoxLayout()
        tempbox = QtWidgets.QHBoxLayout()
        temperature = QtWidgets.QLabel('Температура на борту')
        temp_value = QtWidgets.QLineEdit()
        tempbox.addWidget(temperature)
        tempbox.addWidget(temp_value)

        razgerm = QtWidgets.QHBoxLayout()
        razgermet = QtWidgets.QLabel('Разгерметизация')
        razgermet_value = QtWidgets.QLineEdit()
        razgerm.addWidget(razgermet)
        razgerm.addWidget(razgermet_value)

        vbox.addLayout(tempbox)
        vbox.addLayout(razgerm)

        tanks = {'tank1': 'Бак №1', 'tank2': 'Бак №2', 'tank3': 'Бак №3'}

        for tank_, tank_name_ in tanks.items():
            tank = QtWidgets.QHBoxLayout()
            tank_name = QtWidgets.QLabel(tank_name_)
            tank_value = QtWidgets.QLineEdit()
            tank.addWidget(tank_name)
            tank.addWidget(tank_value)
            vbox.addLayout(tank)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.resize(300, 100)
    window.setWindowTitle('Параметры корабля')
    window.show()

    app.exec_()
