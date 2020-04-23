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
from SomlosKloningModul import *
from Function import *
from PIL import Image
from functools import partial

class Seamless(QMainWindow):
    def __init__(self):
        super(Seamless, self).__init__()
        uic.loadUi('UI/somlos.ui', self)
        self.path = "../../hdr-bilder/Tree/Tree_00064.png"
        self.seamlessImg.setPixmap(QtGui.QPixmap(self.path))

        self.imgOne = "../../hdr-bilder/Balls/Balls_00016.png"
        self.imgTwo = "../../hdr-bilder/Tree/Tree_00064.png"
        self.imgThree = ""
        self.imgFour = "../../hdr-bilder/MtTamNorth/MtTamNorth_00008.png"
        self.imgFive = ""
        self.imgSix = "../../hdr-bilder/MtTamWest/MtTamWest_00008.png"
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
        self.seamlessOne.clicked.connect(self.seamlessImageOne)
        #self.seamlessTwo.clicked.connect(self.seamlessImageTwo)
        #self.seamlessThree.clicked.connect(self.seamlessImageThree)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 720)
        self.dialog.show()

    def setImage(self, img):
        self.path = img
        self.seamlessImg.setPixmap(QtGui.QPixmap(img))

    def seamlessImageOne(self):
        if not self.imgOneReady:
            self.seamlessImageOne = seamless(self.imgOne, self.imgTwo)
            self.imgOneReady = True
        self.showImage(self.seamlessImageOne)
        
    def seamlessImageTwo(self):
        self.showImage(self.seamlessImageTwo)

    def seamlessImageThree(self):
        self.showImage(self.seamlessImageThree)

    def showImage(self, im):
        im = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(im)
        img.save('pic.png')
        self.seamlessImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')