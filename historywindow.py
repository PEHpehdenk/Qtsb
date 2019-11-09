# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historywindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HistoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        HistoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HistoryWindow)
        QtCore.QMetaObject.connectSlotsByName(HistoryWindow)

    def retranslateUi(self, HistoryWindow):
        _translate = QtCore.QCoreApplication.translate
        HistoryWindow.setWindowTitle(_translate("HistoryWindow", "MainWindow"))
