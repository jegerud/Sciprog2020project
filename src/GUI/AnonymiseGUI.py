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
import sys
sys.path.insert(0, '../')
from Source.Grayscale import rgb2gray
from Source.Anonymise import blurFace, detectFace
from GUI.FunctionGUI import ShowCode
import cv2


class AnonymiseFaces(QMainWindow):
    def __init__(self, app):
        super(AnonymiseFaces, self).__init__()
        uic.loadUi('gui/UI/anonymise.ui', self)
        self.setWindowIcon(QtGui.QIcon('gui/Resources/logo.png'))
        self.setWindowTitle('Anonymisering')
        self.path = "../hdr-bilder/Faces/group1.jpg"
        self.anonymiseImg.setPixmap(QtGui.QPixmap(self.path))
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
    
    def setImage(self, img):
        self.path = img
        self.anonymiseImg.setPixmap(QtGui.QPixmap(img))
        self.updateCount(0)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('gui/codes/anonymisering.txt').read()
        title = "Anonymisering - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 650, 900)
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

    def showFaces(self, image):
        qImg = QtGui.QImage()
        height, width, channels = image.shape
        bytesPerLine = channels * width
        qImg = QtGui.QImage(image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.anonymiseImg.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def numpyQImage(self, image):
        qImg = QtGui.QImage()
        if image.dtype == np.uint8:
            if len(image.shape) == 2:
                channels = 1
                height, width = image.shape
                bytesPerLine = channels * width
                qImg = QtGui.QImage(
                    image.data, width, height, bytesPerLine, QtGui.QImage.Format_Indexed8
                )
                qImg.setColorTable([QtGui.qRgb(i, i, i) for i in range(256)])
            elif len(image.shape) == 3:
                if image.shape[2] == 3:
                    height, width, channels = image.shape
                    bytesPerLine = channels * width
                    qImg = QtGui.QImage(
                        image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888
                    )
                elif image.shape[2] == 4:
                    height, width, channels = image.shape
                    bytesPerLine = channels * width
                    fmt = QtGui.QImage.Format_ARGB32
                    qImg = QtGui.QImage(
                        image.data, width, height, bytesPerLine, QtGui.QImage.Format_ARGB32
                    )
        return qImg

    def updateCount(self, count):
        self.faceCount.setText(str(count))

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