from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget
from Source.Blur import eksplisittGlatting
from Source.Grayscale import rgb2gray, grayscale
from Source.implisitt import implisitt

class Blur(QMainWindow):
    def __init__(self, app):
        super(Blur, self).__init__()
        uic.loadUi('blur.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Glatting')
        self.path = "../hdr-bilder/Balls/Balls_00032.png"
        self.image = imageio.imread(self.path)
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
        self.blurCode.clicked.connect(self.showCode)
        self.blurOriginal.clicked.connect(self.setOriginal)
        self.blurOriginal2.clicked.connect(self.setOriginal)
        self.blurOrigGray.clicked.connect(self.setGray)
        self.blurOrigGray2.clicked.connect(self.setGray)
        self.blurGray.clicked.connect(partial(self.blurImage, False))
        self.blurColour.clicked.connect(partial(self.blurImage, True))
        self.blurGrayIm.clicked.connect(partial(self.blurImageImplisitt, False))
        self.blurColourIm.clicked.connect(partial(self.blurImageImplisitt, True))
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")

    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.showImage(image)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/glatting.txt').read()
        title = "Glatting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 550, 800)
        self.dialog.show()

    def setOriginal(self):
        image = imageio.imread(self.path)
        self.showImage(image)

    def setGray(self):
        self.setOriginal()
        self.showImage(rgb2gray(self.path), False)

    def blurImage(self, colour=True):
        if colour:
            orig_im = imageio.imread(self.path).astype(float)/255 
        else:
            orig_im = rgb2gray(self.path)
        im = np.copy(orig_im)
        im = im + .05 * np.random.randn(* np.shape(im))
        self.showImage(eksplisittGlatting(im, orig_im, self.constant.value()), colour)

    def blurImageImplisitt(self, colour=True):
        if colour:
            u = imageio.imread(self.path)
        else:    
            u = grayscale(self.path)  
        u = u.astype(float) / 255
        u[u<0]=0
        u[u>1]=1
        self.showImage(implisitt(u, n=2, alpha=2.5,rgb=colour), colour)

    def showImage(self, im, colour=True):
        if not colour:
            self.image = np.sum(self.image.astype(float),2) /(3*255)
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
            height = int(screenHeight / 1.97)
        else:
            width = int(screenWidth / 2.22222)
            height = int(screenHeight / 2.25)
        self.setGeometry(520, 100, width, height)