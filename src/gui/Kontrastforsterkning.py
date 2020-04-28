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
from Eksplisitt import eksplisittKontrast
from Function import *
from PIL import Image
from functools import partial

class ContrastEnhancement(QMainWindow):
    def __init__(self):
        super(ContrastEnhancement, self).__init__()
        uic.loadUi('UI/kontrastforsterkning.ui', self)
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.contrastImg.setPixmap(QtGui.QPixmap(self.path))

        self.imgOne = "../../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.imgTwo = "../../hdr-bilder/Balls/Balls_00032.png"
        self.imgThree = "../../hdr-bilder/Fog/Fog_00128.png"
        self.imgFour = "../../hdr-bilder/Garden/Garden_00004.png"
        self.imgFive = "../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgSix = "../../hdr-bilder/Ocean/Ocean_00256.png"
        self.imgSeven = "../../hdr-bilder/StillLife/StillLife_01024.png"
        self.imgEight = "../../hdr-bilder/Tree/Tree_00064.png"

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
        self.demosaicImg.setPixmap(QtGui.QPixmap(img))

    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/kontrastforsterkning.txt').read()
        title = "Kontrastforsterkning Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 750)
        self.dialog.show()

    def setOriginal(self):
        self.contrastImg.setPixmap(QtGui.QPixmap(self.path))

    def setGray(self):
        self.showContrastImage(gray.rgb2gray(self.path))

    def contrastImage(self):
        orig_im = imageio.imread(self.path).astype(float)/255 
        im = np.copy(orig_im)
        self.showContrastImage(eksplisittKontrast(im, orig_im, self.constant.value()))

    def contrastGrayImage(self):
        orig_im =  gray.rgb2gray(self.path)
        im =  gray.rgb2gray(self.path)
        self.showContrastImage(eksplisittKontrast(im, orig_im, self.constant.value()))

    def showContrastImage(self, im):
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('pic.png')
        self.contrastImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')