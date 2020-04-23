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
from InpaintingModul import *
from Function import *
from PIL import Image

class Inpainting(QMainWindow):
    def __init__(self):
        super(Inpainting, self).__init__()
        uic.loadUi('UI/inpainting.ui', self)
        self.path = "../../hdr-bilder/Tree/Tree_00064.png"
        self.inpaintImg.setPixmap(QtGui.QPixmap(self.path))

        self.inpaintingCode.clicked.connect(self.showCode)
        self.imageOne.clicked.connect(self.setImg1)
        self.imageTwo.clicked.connect(self.setImg2)
        self.imageThree.clicked.connect(self.setImg3)
        self.maskOne.clicked.connect(self.showMask)
        self.maskTwo.clicked.connect(self.showMask)
        self.maskThree.clicked.connect(self.showMask)
        self.inpaintOne.clicked.connect(self.inpaint)
        self.inpaintTwo.clicked.connect(self.inpaint)
        self.inpaintThree.clicked.connect(self.inpaint)
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/inpainting.txt').read()
        title = "Inpainting - kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 600, 720)
        self.dialog.show()

    def setImg1(self):
        self.path = "../../hdr-bilder/Tree/Tree_00064.png"
        self.inpaintImg.setPixmap(QtGui.QPixmap(self.path))

    def setImg2(self):
        self.path = "../../hdr-bilder/Fog/Fog_00512.png"
        self.inpaintImg.setPixmap(QtGui.QPixmap(self.path))
    
    def setImg3(self):
        self.path = "../../hdr-bilder/MtTamNorth/MtTamNorth_00008.png"
        self.inpaintImg.setPixmap(QtGui.QPixmap(self.path))

    def showMask(self):
        self.showImage(Inpaint(self.path, 2), False)

    def inpaint(self):
        self.showImage(Inpaint_rgb(self.path, 3))

    def showImage(self, im, colour=True):
        if colour: 
            im = (255.0 / im.max() * (im - im.min())).astype(np.uint8)
        img = Image.fromarray(im)
        img.save('pic.png')
        self.inpaintImg.setPixmap(QtGui.QPixmap('pic.png'))
        os.remove('pic.png')