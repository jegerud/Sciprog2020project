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
import sys
sys.path.insert(0, '../')
from Source.Inpainting import Inpaint
from gui.FunctionGUI import ShowCode

class Inpainting(QMainWindow):
    def __init__(self):
        super(Inpainting, self).__init__()
        uic.loadUi('gui/UI/inpainting.ui', self)
        self.path = "../hdr-bilder/Tree/Tree_00064.png"
        self.inpaintImg.setPixmap(QtGui.QPixmap(self.path))
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
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('gui/codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 720)
        self.dialog.show()

    def setImage(self, img):
        self.path = img
        self.inpaintImg.setPixmap(QtGui.QPixmap(img))

    def showMask(self):
        self.showImage(Inpaint(self.path, 2), False)

    def inpaint(self):
        self.showImage(Inpaint(self.path, 3))

    def showImage(self, im, colour=True):
        if colour: 
            im = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(im)
        img.save('pic.png')
        self.inpaintImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')