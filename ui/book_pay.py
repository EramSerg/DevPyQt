from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setMinimumSize(250, 150)
        self.setMaximumSize(1500, 750)

        mainbox = QtWidgets.QVBoxLayout()

        grp_box = QtWidgets.QGroupBox(self)
        grp_box.setTitle('Выберите книгу')
        grp_box.setMinimumSize(100, 50)
        grp_box.setMaximumSize(700, 350)
        text = QtWidgets.QTextBrowser()
        text.setMarkdown('Гарри Поттер')

        # GroupBox выбора варианта оплаты
        grp_box_pay = QtWidgets.QGroupBox(self)
        grp_box_pay.setTitle('Выберите способ оплаты')
        grp_box_pay.setMinimumSize(100, 50)
        grp_box_pay.setMaximumSize(700, 350)
        buttonbox = QtWidgets.QVBoxLayout()
        button1 = QtWidgets.QRadioButton('Карта')
        button2 = QtWidgets.QRadioButton('СБП')
        button3 = QtWidgets.QRadioButton('QR')
        buttonbox.addWidget(button1)
        buttonbox.addWidget(button2)
        buttonbox.addWidget(button3)
        grp_box_pay.setLayout(buttonbox)

        mainbox.addWidget(grp_box)
        mainbox.addWidget(grp_box_pay)
        self.setLayout(mainbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.setWindowTitle('Авторизация')
    window.resize(300, 100)
    window.show()

    app.exec_()