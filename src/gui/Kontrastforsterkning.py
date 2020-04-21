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
from GlattingModul import eksplisittGlatting
from Function import *
from PIL import Image

class Kontrastforsterkning(QMainWindow):
    def __init__(self):
        super(Kontrastforsterkning, self).__init__()
        uic.loadUi('UI/kontrastforsterkning.ui', self)
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.kontrastBilde.setPixmap(QtGui.QPixmap(self.path))

        self.adjuster.clicked.connect(self.showAdjuster)
        self.balls.clicked.connect(self.showBalls)
        self.fog.clicked.connect(self.showFog)
        self.garden.clicked.connect(self.showGarden)
        self.mountains.clicked.connect(self.showMountains)
        self.ocean.clicked.connect(self.showOcean)
        self.stillife.clicked.connect(self.showStillife)
        self.trees.clicked.connect(self.showTrees)

    def showAdjuster(self):
        self.path = "../../hdr-bilder/Adjuster/Adjuster_00032.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def showBalls(self):
        self.path = "../../hdr-bilder/Balls/Balls_00032.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def showFog(self):
        self.path = "../../hdr-bilder/Fog/Fog_00128.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def showGarden(self):
        self.path = "../../hdr-bilder/Garden/Garden_00004.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def showMountains(self):
        self.path = "../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def showOcean(self):
        self.path = "../../hdr-bilder/Ocean/Ocean_00256.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))
    
    def showStillife(self):
        self.path = "../../hdr-bilder/StillLife/StillLife_01024.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def showTrees(self):
        self.path = "../../hdr-bilder/Tree/Tree_00064.png"
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/glatting.txt').read()
        title = "Glatting kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title)
        self.dialog.show()

    def setOriginal(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap(self.path))

    def setGray(self):
        im = gray.rgb2gray(self.path)
        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('test.png')
        self.glattingBilde.setPixmap(QtGui.QPixmap('test.png'))
        os.remove('test.png')

    def blurImage(self):
        orig_im = imageio.imread(self.path).astype(float)/255 
        im = np.copy(orig_im)
        im = im + .05 * np.random.randn(* np.shape(im))
        im = eksplisittGlatting(im, orig_im, self.konstant.value())

        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('test.png')
        self.glattingBilde.setPixmap(QtGui.QPixmap('test.png'))
        os.remove('test.png')

    def blurGrayImage(self):
        orig_im =  gray.rgb2gray(self.path)
        im =  gray.rgb2gray(self.path)
        im = im + .05 * np.random.randn(* np.shape(im))
        im = eksplisittGlatting(im, orig_im, self.konstant.value())

        rescaled = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(rescaled)
        img.save('test.png')
        self.glattingBilde.setPixmap(QtGui.QPixmap('test.png'))
        os.remove('test.png')