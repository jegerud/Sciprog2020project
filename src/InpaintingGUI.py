from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from Source.Inpainting import maskImage, Inpaint
from Source.Grayscale import rgb2gray
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget


class Inpainting(QMainWindow):
    def __init__(self, app):
        super(Inpainting, self).__init__()
        uic.loadUi('inpainting.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Inpainting')
        self.number = 0
        self.adjustScreen(app)
        self.imgOne = imageio.imread(self.getPath(1))
        self.imgTwo = imageio.imread(self.getPath(2))
        self.imgThree = imageio.imread(self.getPath(3))

        self.inpaintingCode.clicked.connect(self.showCode)
        self.imageOne.clicked.connect(partial(self.setImage, 1))
        self.imageTwo.clicked.connect(partial(self.setImage, 2))
        self.imageThree.clicked.connect(partial(self.setImage, 3))
        self.maskOne.clicked.connect(partial(self.showMask, 1))
        self.maskTwo.clicked.connect(partial(self.showMask, 2))
        self.maskThree.clicked.connect(partial(self.showMask, 3))
        self.inpaintOne.clicked.connect(partial(self.inpaint, 1))
        self.inpaintTwo.clicked.connect(partial(self.inpaint, 2))
        self.inpaintThree.clicked.connect(partial(self.inpaint, 3))
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")
        self.setImage(1)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 570, 720)
        self.dialog.show()

    def setImage(self, number):
        self.number = number
        image = imageio.imread(self.getPath(number))
        self.showImage(image)

    def showMask(self, number):
        self.number = number
        self.showImage(maskImage(self.getPath(number)), False)

    def inpaint(self, number):
        self.number = number
        self.showImage(Inpaint(self.getPath(number)))

    def showImage(self, im, colour=True):
        if self.number == 1: self.imgOne = im.copy() 
        elif self.number == 2: self.imgTwo = im.copy()
        elif self.number == 3: self.imgThree = im.copy()
        self.imagewidget.showImage(im, colour)

    def getPath(self, nr):
        if nr == 1: return "../hdr-bilder/Tree/Tree_00064.png"
        elif nr == 2: return "../hdr-bilder/Faces/group3.jpg"
        elif nr == 3: return "../hdr-bilder/MtTamNorth/MtTamNorth_00008.png"

    def saveImage(self):
        if self.number == 1: saveImage(self.imgOne)
        elif self.number == 2: saveImage(self.imgTwo)
        elif self.number == 3: saveImage(self.imgThree)

    def adjustScreen(self, app):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.75)
            height = int(screenHeight / 2.2)
        else:
            width = int(screenWidth / 2.22222)
            height = int(screenHeight / 2.2)
        self.setGeometry(520, 100, width, height)