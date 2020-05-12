from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from Source.Demosaicing import *
from Source.Grayscale import rgb2gray
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget

class Demosaic(QMainWindow):
    def __init__(self, app):
        super(Demosaic, self).__init__()
        uic.loadUi('demosaicing.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Demosaicing')
        self.path = "../hdr-bilder/Balls/Balls_00032.png"
        self.image = imageio.imread(self.path)
        self.setImage(self.path)
        self.adjustScreen(app)

        self.imgOne = "../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.imgTwo = "../hdr-bilder/Balls/Balls_00032.png"
        self.imgThree = "../hdr-bilder/Faces/group1.jpg"
        self.imgFour = "../hdr-bilder/Faces/business.jpg"
        self.imgFive = "../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgSix = "../hdr-bilder/Ocean/Ocean_00256.png"
        self.imgSeven = "../hdr-bilder/StillLife/StillLife_01024.png"
        self.imgEight = "../hdr-bilder/Tree/Tree_00064.png"

        self.adjuster.clicked.connect(partial(self.setImage, self.imgOne))
        self.balls.clicked.connect(partial(self.setImage, self.imgTwo))
        self.group.clicked.connect(partial(self.setImage, self.imgThree))
        self.business.clicked.connect(partial(self.setImage, self.imgFour))
        self.mountains.clicked.connect(partial(self.setImage, self.imgFive))
        self.ocean.clicked.connect(partial(self.setImage, self.imgSix))
        self.stillife.clicked.connect(partial(self.setImage, self.imgSeven))
        self.trees.clicked.connect(partial(self.setImage, self.imgEight))
        self.demosaicCode.clicked.connect(self.showCode)
        self.demosaicOriginal.clicked.connect(self.setOriginal)
        self.demosaicOriginal2.clicked.connect(self.setOriginal)
        self.demosaicMosaic.clicked.connect(self.mosaic)
        self.demosaicMosaicPackage.clicked.connect(self.mosaicPackage)
        self.demosaicDemosaic.clicked.connect(self.demosaicImage)
        self.demosaicDemosaicPackage.clicked.connect(self.demosaicImagePackage)
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")

    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.showImage(image)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/demosaicing.txt').read()
        title = "Demosaicing - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 800)
        self.dialog.show()

    def setOriginal(self):
        image = imageio.imread(self.path)
        self.showImage(image)

    def mosaic(self):
        self.showImage(getMosaic(self.path), False)

    def mosaicPackage(self):
        self.showImage(getMosaicPackage(self.path), False)

    def demosaicImage(self):
        self.showImage(mosaicToRgb(self.path))

    def demosaicImagePackage(self):
        self.showImage(mosaicToRgbPackage(self.path))

    def showImage(self, im, colour=True):
        if not colour:
            self.image = rgb2gray(self.path)
        else:
            self.image = imageio.imread(self.path)
        np.reshape(self.image, im.shape)
        self.image = im.copy()
        self.imagewidget.showImage(im, colour)

    def saveImage(self):
        saveImage(self.image)

    def adjustScreen(self, app):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.73)
            height = int(screenHeight / 2.12)
        else:
            width = int(screenWidth / 2.22222)
            height = int(screenHeight / 2.2)
        self.setGeometry(520, 100, width, height)