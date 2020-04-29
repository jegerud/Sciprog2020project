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
from Source.Blur import eksplisittGlatting
from GUI.FunctionGUI import ShowCode

class Blur(QMainWindow):
    def __init__(self):
        super(Blur, self).__init__()
        uic.loadUi('gui/UI/blur.ui', self)
        self.setWindowIcon(QtGui.QIcon('gui/Resources/logo.png'))
        self.path = "../hdr-bilder/Balls/Balls_00032.png"
        self.blurImg.setPixmap(QtGui.QPixmap(self.path))

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
        self.blurCode.clicked.connect(self.showCode)
        self.blurGray.clicked.connect(self.blurGrayImage)
        self.blurOriginal.clicked.connect(self.setOriginal)
        self.blurColour.clicked.connect(self.blurImage)
        self.blurOrigGray.clicked.connect(self.setGray)

    def setImage(self, img):
        self.path = img
        self.blurImg.setPixmap(QtGui.QPixmap(img))
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('gui/codes/glatting.txt').read()
        title = "Glatting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 400)
        self.dialog.show()

    def setOriginal(self):
        self.blurImg.setPixmap(QtGui.QPixmap(self.path))

    def setGray(self):
        self.showBlurImage(rgb2gray(self.path))

    def blurImage(self):
        orig_im = imageio.imread(self.path).astype(float)/255 
        im = np.copy(orig_im)
        im = im + .05 * np.random.randn(* np.shape(im))
        self.showBlurImage(eksplisittGlatting(im, orig_im, self.constant.value()))

    def blurGrayImage(self):
        orig_im = rgb2gray(self.path)
        im = rgb2gray(self.path)
        im = im + .05 * np.random.randn(* np.shape(im))
        self.showBlurImage(im = eksplisittGlatting(im, orig_im, self.constant.value()))

    def showBlurImage(self, im):
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('pic.png')
        self.blurImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')