from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
from Source.SeamlessCloning import seamless
from FunctionGUI import ShowCode, saveImage
from imagewidget import imagewidget
import imageio
import numpy as np
import matplotlib.pyplot as plt

class Seamless(QMainWindow):
    def __init__(self, app):
        super(Seamless, self).__init__()
        uic.loadUi('seamless.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Sømløs kloning')
        self.adjustScreen(app)
        self.number = 1

        self.imgOne = "../hdr-bilder/Balls/Balls_00016.png"
        self.imgTwo = "../hdr-bilder/Tree/Tree_00064.png"
        self.imgThree = "../hdr-bilder/Seamless/bear.jpg"
        self.imgThreeOriginal = "../hdr-bilder/Seamless/bearOriginal.jpg"
        self.imgFour = "../hdr-bilder/Seamless/Abid.jpg"
        self.imgFive = "../hdr-bilder/Seamless/donald.jpg"
        self.imgSix = "../hdr-bilder/Seamless/baby.jpg"
        self.imgOneReady = False
        self.imgTwoReady = False
        self.imgThreeReady = False
        self.imageOne = imageio.imread(self.imgTwo)
        self.imageTwo = imageio.imread(self.imgFour)
        self.imageThree = imageio.imread(self.imgSix)
        self.setImage(self.imgTwo, self.number)

        self.seamlessCode.clicked.connect(self.showCode)
        self.imageOneOne.clicked.connect(partial(self.setImage, self.imgOne, 1))
        self.imageOneTwo.clicked.connect(partial(self.setImage, self.imgTwo, 1))
        self.imageTwoOne.clicked.connect(partial(self.setImage, self.imgThreeOriginal, 2))
        self.imageTwoTwo.clicked.connect(partial(self.setImage, self.imgFour, 2))
        self.imageThreeOne.clicked.connect(partial(self.setImage, self.imgFive, 3))
        self.imageThreeTwo.clicked.connect(partial(self.setImage, self.imgSix, 3))
        self.seamlessOne.clicked.connect(partial(self.seamlessImage, 1))
        self.seamlessTwo.clicked.connect(partial(self.seamlessImage, 2))
        self.seamlessThree.clicked.connect(partial(self.seamlessImage, 3))
        self.save.clicked.connect(self.saveImage)
        self.save.setShortcut("Ctrl+S")

    def showCode(self, nr):
        code = QPlainTextEdit()
        text = open('codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 720)
        self.dialog.show()

    def setImage(self, img, nr):
        self.path = img
        image = imageio.imread(img)
        self.showImage(image)
        self.number = nr

    def seamlessImage(self, number):
        if number == 1:
            if not self.imgOneReady:
                xy0 = (700,50)
                xy1 = (350,500)
                xlen = 200
                ylen = 500
                self.imageOne = seamless(self.imgOne, self.imgTwo, xy0, xy1, xlen, ylen)
                self.imgOneReady = True 
            self.showImage(self.imageOne)
        elif number == 2:
            if not self.imgTwoReady:
                xy0 = (400,265)
                xy1 = (0,0)    
                xlen = 173      
                ylen = 160
                self.imageTwo = seamless(self.imgThree, self.imgFour, xy0, xy1, xlen, ylen)
                self.imgTwoReady = True 
            self.showImage(self.imageTwo)
        elif number == 3:
            if not self.imgThreeReady:
                xy0 = (340,820)
                xy1 = (240,590)    
                xlen = 300      
                ylen = 260     
                self.imageThree = seamless(self.imgFive, self.imgSix, xy0, xy1, xlen, ylen)
                self.imgThreeReady = True 
            self.showImage(self.imageThree)    

    def showImage(self, im):
        self.image = imageio.imread(self.path)
        np.reshape(self.image, im.shape)
        self.image = im.copy()
        self.imagewidget.showImage(im)

    def saveImage(self):
        if self.number == 1: saveImage(self.imageOne)
        elif self.number == 2: saveImage(self.imageTwo)
        elif self.number == 3: saveImage(self.imageThree)

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