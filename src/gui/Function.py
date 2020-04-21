from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ShowCode(QDialog):
    def __init__(self, text, title, height, parent=None):
        super(ShowCode, self).__init__(parent)
        self.setWindowTitle(title)
        self.setGeometry(500, 80, 500, height)
        codeLabel = QtWidgets.QLabel(self)
        codeLabel.setText(text)
        codeLabel.move(10, 20)
        codeLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
