from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
import cv2
from PIL import Image

class ShowCode(QMainWindow):
    def __init__(self, text, title, width, height, parent=None):
        super(ShowCode, self).__init__(parent)
        uic.loadUi('function.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle(title)
        self.setGeometry(500, 80, width, height)
        self.code.setText(text)
        self.code.setTextInteractionFlags(Qt.TextSelectableByMouse)

def saveImage(image):
    name, ok = QFileDialog.getSaveFileName(None, "Lagre bilde", "", "PNG (*.png);;JPG (*.jpg)")
    if ok and name:
        try:
            if ok[:3] == "PNG" and name[-3:] != "png":
                name = name + '.png'
            elif ok[:3] == "JPG" and name[-3:] != "jpg":
                name = name + '.jpg'
            image = np.round(image*255).astype('uint8')
            cv2.imwrite(name, image)
        except:
            print("Error, bilde kunne ikke lagres")