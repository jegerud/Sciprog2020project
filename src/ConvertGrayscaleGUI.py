from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from Source.Grayscale import rgb2gray, grayscale
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget


class GrayscaleConvert(QMainWindow):
    def __init__(self, app):
        super(GrayscaleConvert, self).__init__()
        uic.loadUi('convertgrayscale.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Konvertering til gråtone')
        self.path = "../hdr-bilder/Balls/Balls_00032.png"
        self.image = imageio.imread(self.path)
        self.setImage(self.path)
        self.adjustScreen(app)

        self.imgOne = "../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.imgTwo = "../hdr-bilder/Balls/Balls_00032.png"
        self.imgThree = "../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgFour = "../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgFive = "../hdr-bilder/Ocean/Ocean_00256.png"
        self.imgSix = "../hdr-bilder/StillLife/StillLife_01024.png"
        self.imgSeven = "../hdr-bilder/Tree/Tree_00064.png"
        self.imgEigth = "../hdr-bilder/Faces/group1.jpg"

        self.adjuster.clicked.connect(partial(self.setImage, self.imgOne))
        self.balls.clicked.connect(partial(self.setImage, self.imgTwo))
        self.mtTamW.clicked.connect(partial(self.setImage, self.imgThree))
        self.mtTamN.clicked.connect(partial(self.setImage, self.imgFour))
        self.ocean.clicked.connect(partial(self.setImage, self.imgFive))
        self.stillife.clicked.connect(partial(self.setImage, self.imgSix))
        self.trees.clicked.connect(partial(self.setImage, self.imgSeven))
        self.group.clicked.connect(partial(self.setImage, self.imgEigth))
        self.grayCode.clicked.connect(self.showCode)
        self.grayOriginal.clicked.connect(self.setOriginal)
        self.grayEasy.clicked.connect(self.convertGrayEasy)
        self.grayAdvanced.clicked.connect(self.convertGrayAdvanced)
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")

    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.showImage(image)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/grayscaleConvert.txt').read()
        title = "Konvertering til gråtone - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 500, 780)
        self.dialog.show()

    def setOriginal(self):
        image = imageio.imread(self.path)
        self.showImage(image)

    def convertGrayEasy(self):
        self.showImage(grayscale(self.path), False)

    def convertGrayAdvanced(self):
        self.showImage(rgb2gray(self.path), False)

    def showImage(self, im, colour=True):
        if not colour:
            self.image = rgb2gray(self.path)
        else:
            self.image = imageio.imread(self.path)
        np.reshape(self.image, im.shape)
        self.image = im.copy()
        self.imagewidget.showImage(self.image, colour)

    def saveImage(self, image=0):
        saveImage(self.image)

    def adjustScreen(self, app):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.67)
            height = int(screenHeight / 2.25)
        else:
            width = int(screenWidth / 2.15)
            height = int(screenHeight / 2.4)
        self.setGeometry(520, 100, width, height)