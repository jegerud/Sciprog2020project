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
from DemosaicingModul import *
from Function import *
from PIL import Image

class Demosaic(QMainWindow):
    def __init__(self):
        super(Demosaic, self).__init__()
        uic.loadUi('UI/anonymisering.ui', self)
        self.path = "../../hdr-bilder/faces/lfc.jpeg"
        self.faceCount = "2"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

        self.adjuster.clicked.connect(self.showAdjuster)
        self.balls.clicked.connect(self.showBalls)
        self.fog.clicked.connect(self.showFog)
        self.garden.clicked.connect(self.showGarden)
        self.mountains.clicked.connect(self.showMountains)
        self.ocean.clicked.connect(self.showOcean)
        self.stillife.clicked.connect(self.showStillife)
        self.trees.clicked.connect(self.showTrees)
        self.demosaicCode.clicked.connect(self.showCode)
        self.demosaicOriginal.clicked.connect(self.setOriginal)
        self.demosaicOriginal2.clicked.connect(self.setOriginal)
        self.demosaicMosaic.clicked.connect(self.mosaic)
        self.demosaicMosaicPackage.clicked.connect(self.mosaicPackage)
        self.demosaicDemosaic.clicked.connect(self.demosaicImage)
        self.demosaicDemosaicPackage.clicked.connect(self.demosaicImagePackage)

    def showAdjuster(self):
        self.path = "../../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def showBalls(self):
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def showFog(self):
        self.path = "../../hdr-bilder/Fog/Fog_00128.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def showGarden(self):
        self.path = "../../hdr-bilder/Garden/Garden_00004.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def showMountains(self):
        self.path = "../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def showOcean(self):
        self.path = "../../hdr-bilder/Ocean/Ocean_00256.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))
    
    def showStillife(self):
        self.path = "../../hdr-bilder/StillLife/StillLife_01024.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def showTrees(self):
        self.path = "../../hdr-bilder/Tree/Tree_00064.png"
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/demosaicing.txt').read()
        title = "Demosaicing - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 650, 700)
        self.dialog.show()

    def setOriginal(self):
        self.demosaicImg.setPixmap(QtGui.QPixmap(self.path))

    def mosaic(self):
        mosaic = getMosaic(self.path)
        self.showImage(img)

    def mosaicPackage(self):
        mosaic = getMosaicPackage(self.path)

    def demosaicImage(self):
        img = mosaicToRgb(self.path)
        self.showFaces(img)

    def demosaicImagePackage(self):
        img = mosaicToRgbPackage(self.path)
        self.showFaces(img)

    def showImage(self, im):
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('pic.png')
        self.demosaicImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')