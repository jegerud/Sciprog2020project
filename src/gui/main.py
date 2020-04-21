from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Glatting import *
import sys

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('UI/mainWindow.ui', self)

        self.openGlatting.clicked.connect(self.onOpenGlattingClicked)
        self.dialog = Glatting()
    
    def onOpenGlattingClicked(self):
        self.dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())