from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui import *
import sys

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('gui/UI/mainWindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))

        self.openBlur.clicked.connect(self.onOpenBlurClicked)
        self.openInpainting.clicked.connect(self.onOpenInpaintingClicked)
        self.openContrast.clicked.connect(self.onOpenContrastClicked)
        self.openDemosaicing.clicked.connect(self.onOpenDemosaicingClicked)
        self.openSeamless.clicked.connect(self.onOpenSeamlessClicked)
        self.openGrayConvert.clicked.connect(self.onOpenGrayscaleClicked)
        self.openAnonymise.clicked.connect(self.onOpenAnonymiseClicked)
    
    def onOpenBlurClicked(self):
        self.dialog = Blur()
        self.dialog.show()
    
    def onOpenInpaintingClicked(self):
        self.dialog = Inpainting()
        self.dialog.show()

    def onOpenContrastClicked(self):
        self.dialog = ContrastEnhancement()
        self.dialog.show()

    def onOpenDemosaicingClicked(self):
        self.dialog = Demosaic()
        self.dialog.show()

    def onOpenSeamlessClicked(self):
        self.dialog = Seamless()
        self.dialog.show()
    
    def onOpenGrayscaleClicked(self):
        self.dialog = GrayscaleConvert()
        self.dialog.show()

    def onOpenAnonymiseClicked(self):
        self.dialog = AnonymiseFaces()
        self.dialog.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())