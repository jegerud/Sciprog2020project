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
from gui.FunctionGUI import ShowCode

class GrayscaleConvert(QMainWindow):
    def __init__(self):
        super(GrayscaleConvert, self).__init__()
        uic.loadUi('UI/konverteringGraatone.ui', self)
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

        self.imgOne = "../../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.imgTwo = "../../hdr-bilder/Balls/Balls_00032.png"
        self.imgThree = "../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgFour = "../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.imgFive = "../../hdr-bilder/Ocean/Ocean_00256.png"
        self.imgSix = "../../hdr-bilder/StillLife/StillLife_01024.png"
        self.imgSeven = "../../hdr-bilder/Tree/Tree_00064.png"

        self.adjuster.clicked.connect(partial(self.setImage, self.imgOne))
        self.balls.clicked.connect(partial(self.setImage, self.imgTwo))
        self.mtTamW.clicked.connect(partial(self.setImage, self.imgThree))
        self.mtTamN.clicked.connect(partial(self.setImage, self.imgFour))
        self.ocean.clicked.connect(partial(self.setImage, self.imgFive))
        self.stillife.clicked.connect(partial(self.setImage, self.imgSix))
        self.trees.clicked.connect(partial(self.setImage, self.imgSeven))
        self.grayCode.clicked.connect(self.showCode)
        self.grayOriginal.clicked.connect(self.setOriginal)
        self.grayEasy.clicked.connect(self.convertGrayEasy)
        self.grayAdvanced.clicked.connect(self.convertGrayAdvanced)

    def setImage(self, img):
        self.path = img
        self.grayImg.setPixmap(QtGui.QPixmap(img))
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/grayscaleConvert.txt').read()
        title = "Konvertering til gråtone - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 780)
        self.dialog.show()

    def setOriginal(self):
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

    def convertGrayEasy(self):
        self.convertGray(grayscale(self.path))

    def convertGrayAdvanced(self):
        self.convertGray(rgb2gray(self.path))

    def convertGray(self, im):
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('pic.png')
        self.grayImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')