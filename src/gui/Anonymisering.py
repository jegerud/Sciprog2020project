from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

sys.path.insert(0, '../')
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
import Grayscale as gray
from AnonymiseringModul import *
from Function import *
from PIL import Image

class AnonymiseFaces(QMainWindow):
    def __init__(self):
        super(AnonymiseFaces, self).__init__()
        uic.loadUi('UI/anonymisering.ui', self)
        self.path = "../../hdr-bilder/Faces/group.jpg"
        self.anonymiseImg.setPixmap(QtGui.QPixmap(self.path))

        self.lena.clicked.connect(self.showLena)
        self.group1.clicked.connect(self.showGroup)
        self.anonymousCode.clicked.connect(self.showCode)
        self.anonymousOriginal.clicked.connect(self.setOriginal)
        self.anonymousFindFaces.clicked.connect(self.detectFaces)
        self.anonymousAnonymise.clicked.connect(self.anonymiseFaces)

    def showLena(self):
        self.path = "../../hdr-bilder/Faces/lena.png"
        self.anonymiseImg.setPixmap(QtGui.QPixmap(self.path))

    def showGroup(self):
        self.path = "../../hdr-bilder/Faces/group.jpg"
        self.anonymiseImg.setPixmap(QtGui.QPixmap(self.path))
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/anonymisering.txt').read()
        title = "Anonymisering - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 700, 900)
        self.dialog.show()

    def setOriginal(self):
        self.anonymiseImg.setPixmap(QtGui.QPixmap(self.path))
        self.updateCount(0)

    def detectFaces(self):
        count, img = detectFace(self.path)
        self.updateCount(count)
        self.showFaces(img)

    def anonymiseFaces(self):
        count, img = blurFace(self.path)
        self.updateCount(count)
        self.showFaces(img)

    def showFaces(self, im):
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('pic.png')
        self.anonymiseImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')

    def updateCount(self, count):
        self.faceCount.setText(str(count))
