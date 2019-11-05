#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit, QMainWindow
from pygame import mixer  # Sound support
import time
import random

import legacy
from mainwindow import Ui_MainWindow

field = [[[]] * 10] * 10
field2 = [[[]] * 10] * 10

# TODO: Убить Даниэля, кхм, не то...
# TODO: Перенести сюда функцию legacy.randomShip (нормальную!)
def genBattleField():



# TODO: QtDesigner клевая вещь, давайте ее использовать (ну как бы все сразу видно, что как смотрится)


class GameWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
