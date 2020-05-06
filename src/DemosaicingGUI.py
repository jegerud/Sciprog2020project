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
from Source.Demosaicing import *
from FunctionGUI import ShowCode
from imagewidget import imagewidget

class Demosaic(QMainWindow):
    def __init__(self, app):
        super(Demosaic, self).__init__()
        uic.loadUi('demosaicing.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Demosaicing')
        self.path = "../hdr-bilder/Balls/Balls_00032.png"
        self.setImage(self.path)
        self.adjustScreen(app)

        self.imgOne = "../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.imgTwo = "../hdr-bilder/Balls/Balls_00032.png"
        self.imgThree = "../hdr-bilder/Fog/Fog_00128.png"
        self.imgFour = "../hdr-bilder/Garden/Garden_00004.png"
        self.imgFive = "../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgSix = "../hdr-bilder/Ocean/Ocean_00256.png"
        self.imgSeven = "../hdr-bilder/StillLife/StillLife_01024.png"
        self.imgEight = "../hdr-bilder/Tree/Tree_00064.png"

        self.adjuster.clicked.connect(partial(self.setImage, self.imgOne))
        self.balls.clicked.connect(partial(self.setImage, self.imgTwo))
        self.fog.clicked.connect(partial(self.setImage, self.imgThree))
        self.garden.clicked.connect(partial(self.setImage, self.imgFour))
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

    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.imagewidget.showImage(image)
    
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
        mosaic = getMosaic(self.path)
        self.showImage(mosaic, False)

    def mosaicPackage(self):
        mosaic = getMosaicPackage(self.path)
        self.showImage(mosaic, False)

    def demosaicImage(self):
        img = mosaicToRgb(self.path)
        self.showImage(img)

    def demosaicImagePackage(self):
        img = mosaicToRgbPackage(self.path)
        self.showImage(img)

    def showImage(self, im, colour=True):
        self.imagewidget.showImage(im, colour)

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