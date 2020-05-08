from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
from functools import partial
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from Source.Grayscale import rgb2gray
from Source.Anonymise import blurFace, detectFace
from FunctionGUI import ShowCode, saveAnonymiseImage
from imagewidget import imagewidget

class AnonymiseFaces(QMainWindow):
    def __init__(self, app):
        super(AnonymiseFaces, self).__init__()
        uic.loadUi('anonymise.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Anonymisering')
        self.adjustScreen(app)
        self.number = 0
        self.imgCouple = imageio.imread(self.getPath(1))
        self.imgGroup1 = imageio.imread(self.getPath(2))
        self.imgGroup2 = imageio.imread(self.getPath(3))
        self.imgGroup3 = imageio.imread(self.getPath(4))
        self.imgTeam = imageio.imread(self.getPath(5))
        self.imgFamily = imageio.imread(self.getPath(6))
        self.imgBusiness = imageio.imread(self.getPath(7))
        self.setImage(1)
        self.couple.clicked.connect(partial(self.setImage, 1))
        self.group1.clicked.connect(partial(self.setImage, 2))
        self.group2.clicked.connect(partial(self.setImage, 3))
        self.group3.clicked.connect(partial(self.setImage, 4))
        self.team.clicked.connect(partial(self.setImage, 5))
        self.family.clicked.connect(partial(self.setImage, 6))
        self.business.clicked.connect(partial(self.setImage, 7))
        self.anonymousCode.clicked.connect(self.showCode)
        self.anonymousOriginal.clicked.connect(self.setOriginal)
        self.anonymousFindFaces.clicked.connect(self.detectFaces)
        self.anonymousAnonymise.clicked.connect(self.anonymiseFaces)
        self.save.clicked.connect(partial(self.saveImage, self.number))
        self.save.setShortcut("Ctrl+S")
    
    def setImage(self, nr):
        image = imageio.imread(self.getPath(nr))
        self.showImage(image)
        self.number = nr
        self.updateCount(0)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/anonymisering.txt').read()
        title = "Anonymisering - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 650, 900)
        self.dialog.show()

    def setOriginal(self):
        image = imageio.imread(self.getPath(self.number))
        self.showImage(image)
        self.updateCount(0)

    def detectFaces(self):
        count, img = detectFace(self.getPath(self.number))
        self.updateCount(count)
        self.showImage(img)

    def anonymiseFaces(self):
        count, img = blurFace(self.getPath(self.number))
        self.updateCount(count)
        self.showImage(img)

    def showImage(self, image):
        if self.number == 1: self.imgCouple = image.copy()
        elif self.number == 2: self.imgGroup1 = image.copy()
        elif self.number == 3: self.imgGroup2 = image.copy()
        elif self.number == 4: self.imgGroup3 = image.copy()
        elif self.number == 5: self.imgTeam = image.copy()
        elif self.number == 6: self.imgFamily = image.copy()
        elif self.number == 7: self.imgBusiness = image.copy()
        self.imagewidget.showImage(image)

    def updateCount(self, count):
        self.faceCount.setText(str(count))

    def saveImage(self, number):
        if self.number == 1: saveAnonymiseImage(self.imgCouple)
        elif self.number == 2: saveAnonymiseImage(self.imgGroup1)
        elif self.number == 3: saveAnonymiseImage(self.imgGroup2)
        elif self.number == 4: saveAnonymiseImage(self.imgGroup3)
        elif self.number == 5: saveAnonymiseImage(self.imgTeam)
        elif self.number == 6: saveAnonymiseImage(self.imgFamily)
        elif self.number == 7: saveAnonymiseImage(self.imgBusiness)

    def getPath(self, nr):
        if nr == 1: return "../hdr-bilder/Faces/couple.jpg"
        elif nr == 2: return "../hdr-bilder/Faces/group1.jpg"
        elif nr == 3: return "../hdr-bilder/Faces/group2.jpg"
        elif nr == 4: return "../hdr-bilder/Faces/group3.jpg"
        elif nr == 5: return "../hdr-bilder/Faces/team.jpg"
        elif nr == 6: return "../hdr-bilder/Faces/family.jpg"
        elif nr == 7: return "../hdr-bilder/Faces/business.jpg"

    def adjustScreen(self, app):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.75)
            height = int(screenHeight / 2.25)
        else:
            width = int(screenWidth / 2.25)
            height = int(screenHeight / 2.4)
        self.setGeometry(520, 100, width, height)