from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Glatting import *
from Kontrastforsterkning import *
from Demosaicing import *
from KonverteringGraatone import *
from Anonymisering import *
import sys

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('UI/mainWindow.ui', self)

        self.openGlatting.clicked.connect(self.onOpenGlattingClicked)
        self.openInpainting.clicked.connect(self.onOpenInpaintingClicked)
        self.openContrast.clicked.connect(self.onOpenContrastClicked)
        self.openDemosaicing.clicked.connect(self.onOpenDemosaicingClicked)
        self.openSeamless.clicked.connect(self.onOpenSeamlessClicked)
        self.openGrayConvert.clicked.connect(self.onOpenGrayscaleClicked)
        self.openAnonymise.clicked.connect(self.onOpenAnonymiseClicked)

    
    def onOpenGlattingClicked(self):
        self.dialog = Glatting()
        self.dialog.show()
    
    def onOpenInpaintingClicked(self):
        #self.dialog = Glatting()
        #self.dialog.show()
        return 0

    def onOpenContrastClicked(self):
        self.dialog = ContrastEnhancement()
        self.dialog.show()

    def onOpenDemosaicingClicked(self):
        self.dialog = Demosaic()
        self.dialog.show()

    def onOpenSeamlessClicked(self):
        #self.dialog = ()
        #self.dialog.show()
        return 0
    
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