from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt
import sys
import os
import numpy as np
from PIL import Image

class imagewidget(FigureCanvas):
    def __init__(self, parent=None, width=10, height=10, dpi=100):
        self.img = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.img)
        self.setParent(parent)

    def showImage(self, image, colour=True):
        self.img = self.figure.add_subplot(111)
        self.img.axis("off")
        self.figure.subplots_adjust(left=0.001, right=0.999, top=0.999, bottom=0.001)
        if colour:
            self.img.imshow(image)
        else:
            self.img.imshow(image, plt.cm.gray)
        self.draw()
        