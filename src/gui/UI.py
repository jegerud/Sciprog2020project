# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infoTekst = QtWidgets.QLabel(self.centralwidget)
        self.infoTekst.setGeometry(QtCore.QRect(140, 150, 631, 61))
        self.infoTekst.setObjectName("infoTekst")
        self.glattingTekst = QtWidgets.QLabel(self.centralwidget)
        self.glattingTekst.setGeometry(QtCore.QRect(150, 230, 271, 17))
        self.glattingTekst.setObjectName("glattingTekst")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 50, 571, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.openGlatting = QtWidgets.QPushButton(self.centralwidget)
        self.openGlatting.setGeometry(QtCore.QRect(50, 230, 89, 25))
        self.openGlatting.setObjectName("openGlatting")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.infoTekst.setText(_translate("MainWindow", "**Tekst om prosjekt**"))
        self.glattingTekst.setText(_translate("MainWindow", "**Tekst om glatting**"))
        self.label.setText(_translate("MainWindow", "Vitenskapelig Programmering, Prosjekt 2020"))
        self.openGlatting.setText(_translate("MainWindow", "Glatting"))
