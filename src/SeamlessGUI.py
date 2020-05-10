from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
from functools import partial
import imageio
#import os
import numpy as np
import matplotlib.pyplot as plt
from Source.SeamlessCloning import seamless
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget


class Seamless(QMainWindow):
    def __init__(self, app):
        super(Seamless, self).__init__()
        uic.loadUi('seamless.ui', self)
        self.path = "../hdr-bilder/Tree/Tree_00064.png"
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.image = imageio.imread(self.path)
        self.setWindowTitle('Sømløs kloning')
        self.setImage(self.path)
        self.adjustScreen(app)

        self.imgOne = "../hdr-bilder/Balls/Balls_00016.png"
        self.imgTwo = "../hdr-bilder/Tree/Tree_00064.png"
        self.imgThree = ""
        self.imgFour = "../hdr-bilder/MtTamNorth/MtTamNorth_00008.png"
        self.imgFive = ""
        self.imgSix = "../hdr-bilder/MtTamWest/MtTamWest_00008.png"
        self.imgOneReady = False
        self.imgTwoReady = False
        self.imgThreeReady = False

        self.seamlessCode.clicked.connect(self.showCode)
        self.imageOneOne.clicked.connect(partial(self.setImage, self.imgOne))
        self.imageOneTwo.clicked.connect(partial(self.setImage, self.imgTwo))
        self.imageTwoOne.clicked.connect(partial(self.setImage, self.imgOne))
        self.imageTwoTwo.clicked.connect(partial(self.setImage, self.imgFour))
        self.imageThreeOne.clicked.connect(partial(self.setImage, self.imgOne))
        self.imageThreeTwo.clicked.connect(partial(self.setImage, self.imgSix))
        self.seamlessOne.clicked.connect(partial(self.seamlessImage, self.imgOne, self.imgTwo))
        #self.seamlessTwo.clicked.connect(partial(self.seamlessImage, self.imgOne, self.imgTwo))
        #self.seamlessThree.clicked.connect(partial(self.seamlessImage, self.imgOne, self.imgTwo))
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")

    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 720)
        self.dialog.show()

    def setImage(self, img):
        self.path = img
        image = imageio.imread(img)
        self.showImage(image)

    def seamlessImage(self, img1, img2):
        if not self.imgOneReady:
            self.seamlessImageOne = seamless(img1, img2)
            self.imgOneReady = True 
        self.showImage(self.seamlessImageOne)

    def showImage(self, im):
        self.image = imageio.imread(self.path)
        np.reshape(self.image, im.shape)
        self.image = im.copy()
        self.imagewidget.showImage(im)

    def saveImage(self):
        saveImage(self.image)

    def adjustScreen(self, app):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.84)
            height = int(screenHeight / 2.17)
        else:
            width = int(screenWidth / 2.3)
            height = int(screenHeight / 2.3)
        self.setGeometry(520, 100, width, height)