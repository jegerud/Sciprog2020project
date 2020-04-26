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
from Grayscale import *
from Function import *
from PIL import Image

class GrayscaleConvert(QMainWindow):
    def __init__(self):
        super(GrayscaleConvert, self).__init__()
        uic.loadUi('UI/konverteringGraatone.ui', self)
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

        self.adjuster.clicked.connect(self.showAdjuster)
        self.balls.clicked.connect(self.showBalls)
        self.mtTamW.clicked.connect(self.showMtTamW)
        self.mtTamN.clicked.connect(self.showMtTamN)
        self.ocean.clicked.connect(self.showOcean)
        self.stillife.clicked.connect(self.showStillife)
        self.trees.clicked.connect(self.showTrees)
        self.grayCode.clicked.connect(self.showCode)
        self.grayOriginal.clicked.connect(self.setOriginal)
        self.grayEasy.clicked.connect(self.convertGrayEasy)
        self.grayAdvanced.clicked.connect(self.convertGrayAdvanced)

    def showAdjuster(self):
        self.path = "../../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

    def showBalls(self):
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

    def showMtTamW(self):
        self.path = "../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))
    
    def showMtTamN(self):
        self.path = "../../hdr-bilder/MtTamWest/MtTamWest_00004.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

    def showOcean(self):
        self.path = "../../hdr-bilder/Ocean/Ocean_00256.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))
    
    def showStillife(self):
        self.path = "../../hdr-bilder/StillLife/StillLife_01024.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))

    def showTrees(self):
        self.path = "../../hdr-bilder/Tree/Tree_00064.png"
        self.grayImg.setPixmap(QtGui.QPixmap(self.path))
    
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