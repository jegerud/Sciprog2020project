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
from Source.ContrastEnhancement import *
from GUI.FunctionGUI import ShowCode

class ContrastEnhancement(QMainWindow):
    def __init__(self, app):
        super(ContrastEnhancement, self).__init__()
        uic.loadUi('gui/UI/contrastenhancement.ui', self)
        self.setWindowIcon(QtGui.QIcon('gui/Resources/logo.png'))
        self.setWindowTitle('Kontrastforsterkning')
        self.path = "../hdr-bilder/Balls/Balls_00032.png"
        self.contrastImg.setPixmap(QtGui.QPixmap(self.path))
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
        self.contrastCode.clicked.connect(self.showCode)
        self.contrastGray.clicked.connect(self.contrastGrayImage)
        self.contrastOriginal.clicked.connect(self.setOriginal)
        self.contrastColour.clicked.connect(self.contrastImage)
        self.contrastOrigGray.clicked.connect(self.setGray)

    def setImage(self, img):
        self.path = img
        self.contrastImg.setPixmap(QtGui.QPixmap(img))

    def showCode(self):
        code = QPlainTextEdit()
        text = open('gui/codes/kontrastforsterkning.txt').read()
        title = "Kontrastforsterkning - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 500, 850)
        self.dialog.show()

    def setOriginal(self):
        self.contrastImg.setPixmap(QtGui.QPixmap(self.path))

    def setGray(self):
        self.showContrastImage(rgb2gray(self.path))

    def contrastImage(self):
        self.showContrastImage(contrastEnhance(self.path, self.constant.value()))

    def contrastGrayImage(self):
        self.showContrastImage(contrastEnhanceBW(self.path, self.constant.value()))

    def showContrastImage(self, im):
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('pic.png')
        self.contrastImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')

    def adjustScreen(self, app):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.73)
            height = int(screenHeight / 2.25)
        else:
            width = int(screenWidth / 2.22222)
            height = int(screenHeight / 2.4)
        self.setGeometry(520, 100, width, height)