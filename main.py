#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit
from pygame import mixer  # Sound support
import time
import random

field = [[[]] * 10] * 10
field2 = [[[]] * 10] * 10

# TODO: Убить Даниэля, кхм, не то...
# TODO: Перенести сюда функцию legacy.randomShip

# TODO: QtDesigner клевая вещь, давайте ее использовать (ну как бы все сразу видно, что как смотрится)

