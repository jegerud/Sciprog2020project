from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
from PIL import Image


class ShowCode(QMainWindow):
    def __init__(self, text, title, width, height, parent=None):
        super(ShowCode, self).__init__(parent)
        uic.loadUi('UI/function.ui', self)
        self.setWindowTitle(title)
        self.setGeometry(500, 80, width, height)
        self.code.setText(text)
        self.code.setTextInteractionFlags(Qt.TextSelectableByMouse)