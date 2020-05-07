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
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget

class AnonymiseFaces(QMainWindow):
    def __init__(self, app):
        super(AnonymiseFaces, self).__init__()
        uic.loadUi('anonymise.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Anonymisering')
        self.path = "../hdr-bilder/Faces/group1.jpg"
        self.image = imageio.imread(self.path)
        self.setImage(self.path)
        self.adjustScreen(app)

        self.imgCouple = "../hdr-bilder/Faces/couple.jpg"
        self.imgGroup1 = "../hdr-bilder/Faces/group1.jpg"
        self.imgGroup2 = "../hdr-bilder/Faces/group2.jpg"
        self.imgGroup3 = "../hdr-bilder/Faces/group3.jpg"
        self.imgTeam = "../hdr-bilder/Faces/team.jpg"
        self.imgFamily = "../hdr-bilder/Faces/family.jpg"
        self.imgBusiness = "../hdr-bilder/Faces/business.jpg"

        self.couple.clicked.connect(partial(self.setImage, self.imgCouple))
        self.group1.clicked.connect(partial(self.setImage, self.imgGroup1))
        self.group2.clicked.connect(partial(self.setImage, self.imgGroup2))
        self.group3.clicked.connect(partial(self.setImage, self.imgGroup3))
        self.team.clicked.connect(partial(self.setImage, self.imgTeam))
        self.family.clicked.connect(partial(self.setImage, self.imgFamily))
        self.business.clicked.connect(partial(self.setImage, self.imgBusiness))
        self.anonymousCode.clicked.connect(self.showCode)
        self.anonymousOriginal.clicked.connect(self.setOriginal)
        self.anonymousFindFaces.clicked.connect(self.detectFaces)
        self.anonymousAnonymise.clicked.connect(self.anonymiseFaces)
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")
    
    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.imagewidget.showImage(image)
        self.updateCount(0)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/anonymisering.txt').read()
        title = "Anonymisering - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 650, 900)
        self.dialog.show()

    def setOriginal(self):
        image = imageio.imread(self.path)
        self.showImage(image)
        self.updateCount(0)

    def detectFaces(self):
        count, img = detectFace(self.path)
        self.updateCount(count)
        self.showImage(img)

    def anonymiseFaces(self):
        count, img = blurFace(self.path)
        self.updateCount(count)
        self.showImage(img)

    def showImage(self, image):
        np.reshape(self.image, image.shape)
        self.image = image.copy()
        self.imagewidget.showImage(image)

    def updateCount(self, count):
        self.faceCount.setText(str(count))

    def saveImage(self):
        saveImage(self.image, True)

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
