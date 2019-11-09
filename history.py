from PyQt5.QtWidgets import *
from historywindow import Ui_HistoryWindow
import sys
import sqlite3
import datetime

connection = None
cursor = None


def init():
    global connection, cursor
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()


def shutdown():
    global connection, cursor
    connection.commit()
    connection.close()


def new_res(res):
    global connection, cursor
    init()
    cursor.execute('INSERT INTO History(result, datetime) VALUES (?, ?)', (res, datetime.datetime.now()))
    shutdown()


class HistoryWindow(QMainWindow, Ui_HistoryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Исход сражения', 'Дата'])
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem('Загрузка истории игр...'))
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # Loading history...
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()
        res = self.cur.execute('SELECT * FROM `History`')

        self.table.setRowCount(0)
        for gid, result in enumerate(res):
            self.table.setRowCount(self.table.rowCount() + 1)
            date = result[2]
            result = result[1]
            self.table.setItem(gid, 1, QTableWidgetItem(str(date)))
            if result == 1:
                self.table.setItem(gid, 0, QTableWidgetItem('Первый победил'))
            elif result == 2:
                self.table.setItem(gid, 0, QTableWidgetItem('Второй победил'))
            else:
                self.table.setItem(gid, 0, QTableWidgetItem('Кажется кто-то нашел концовку'))


# app = QApplication(sys.argv)
# hw = HistoryWindow()
# hw.show()
# sys.exit(app.exec())
