from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
from PIL import Image
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from Source.Inpainting import Inpaint
from Source.Grayscale import rgb2gray
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget


class Inpainting(QMainWindow):
    def __init__(self, app):
        super(Inpainting, self).__init__()
        uic.loadUi('inpainting.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Inpainting')
        self.path = "../hdr-bilder/Tree/Tree_00064.png"
        self.image = imageio.imread(self.path)
        self.setImage(self.path)
        self.adjustScreen(app)

        self.imgOne = "../hdr-bilder/Tree/Tree_00064.png"
        self.imgTwo = "../hdr-bilder/Fog/Fog_00512.png"
        self.imgThree = "../hdr-bilder/MtTamNorth/MtTamNorth_00008.png"

        self.inpaintingCode.clicked.connect(self.showCode)
        self.imageOne.clicked.connect(partial(self.setImage, self.imgOne))
        self.imageTwo.clicked.connect(partial(self.setImage, self.imgTwo))
        self.imageThree.clicked.connect(partial(self.setImage, self.imgThree))
        self.maskOne.clicked.connect(self.showMask)
        self.maskTwo.clicked.connect(self.showMask)
        self.maskThree.clicked.connect(self.showMask)
        self.inpaintOne.clicked.connect(self.inpaint)
        self.inpaintTwo.clicked.connect(self.inpaint)
        self.inpaintThree.clicked.connect(self.inpaint)
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 570, 720)
        self.dialog.show()

    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.showImage(image)

    def showMask(self):
        self.showImage(Inpaint(self.path, 2), False)

    def inpaint(self):
        self.showImage(Inpaint(self.path, 3))

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
            width = int(screenWidth / 1.75)
            height = int(screenHeight / 2.2)
        else:
            width = int(screenWidth / 2.22222)
            height = int(screenHeight / 2.2)
        self.setGeometry(520, 100, width, height)