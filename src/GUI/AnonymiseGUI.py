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
import Source.Grayscale as gray
from Source.Anonymise import blurFace, detectFace
from FunctionGUI import ShowCode
from PIL import Image
from functools import partial

class AnonymiseFaces(QMainWindow):
    def __init__(self):
        super(AnonymiseFaces, self).__init__()
        uic.loadUi('UI/anonymisering.ui', self)
        self.path = "../../hdr-bilder/Faces/group1.jpg"
        self.anonymiseImg.setPixmap(QtGui.QPixmap(self.path))

        self.imgObama = "../../hdr-bilder/Faces/obama.jpg"
        self.imgGroup1 = "../../hdr-bilder/Faces/group1.jpg"
        self.imgGroup2 = "../../hdr-bilder/Faces/group2.jpg"
        self.imgGroup3 = "../../hdr-bilder/Faces/group3.jpg"
        self.imgTeam = "../../hdr-bilder/Faces/team.jpg"
        self.imgFamily = "../../hdr-bilder/Faces/family.jpg"
        self.imgFamily2 = "../../hdr-bilder/Faces/family2.jpg"

        self.obama.clicked.connect(partial(self.setImage, self.imgObama))
        self.group1.clicked.connect(partial(self.setImage, self.imgGroup1))
        self.group2.clicked.connect(partial(self.setImage, self.imgGroup2))
        self.group3.clicked.connect(partial(self.setImage, self.imgGroup3))
        self.team.clicked.connect(partial(self.setImage, self.imgTeam))
        self.family1.clicked.connect(partial(self.setImage, self.imgFamily))
        self.family2.clicked.connect(partial(self.setImage, self.imgFamily2))
        self.anonymousCode.clicked.connect(self.showCode)
        self.anonymousOriginal.clicked.connect(self.setOriginal)
        self.anonymousFindFaces.clicked.connect(self.detectFaces)
        self.anonymousAnonymise.clicked.connect(self.anonymiseFaces)
    
    def setImage(self, img):
        self.path = img
        self.anonymiseImg.setPixmap(QtGui.QPixmap(img))
        self.updateCount(0)
    
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
