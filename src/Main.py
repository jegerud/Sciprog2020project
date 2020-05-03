from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import BlurGUI
import InpaintingGUI
import ContrastEnhancementGUI
import DemosaicingGUI
import SeamlessGUI
import ConvertGrayscaleGUI
import AnonymiseGUI
import sys

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('Main.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Poisson Bildebehandling')
        self.adjustScreen()

        self.openBlur.clicked.connect(self.onOpenBlurClicked)
        self.openInpainting.clicked.connect(self.onOpenInpaintingClicked)
        self.openContrast.clicked.connect(self.onOpenContrastClicked)
        self.openDemosaicing.clicked.connect(self.onOpenDemosaicingClicked)
        self.openSeamless.clicked.connect(self.onOpenSeamlessClicked)
        self.openGrayConvert.clicked.connect(self.onOpenGrayscaleClicked)
        self.openAnonymise.clicked.connect(self.onOpenAnonymiseClicked)

    def onOpenBlurClicked(self):
        self.dialog = BlurGUI.Blur(app)
        self.dialog.show()

    def onOpenInpaintingClicked(self):
        self.dialog = InpaintingGUI.Inpainting(app)
        self.dialog.show()

    def onOpenContrastClicked(self):
        self.dialog = ContrastEnhancementGUI.ContrastEnhancement(app)
        self.dialog.show()

    def onOpenDemosaicingClicked(self):
        self.dialog = DemosaicingGUI.Demosaic(app)
        self.dialog.show()

    def onOpenSeamlessClicked(self):
        self.dialog = SeamlessGUI.Seamless(app)
        self.dialog.show()
    
    def onOpenGrayscaleClicked(self):
        self.dialog = ConvertGrayscaleGUI.GrayscaleConvert(app)
        self.dialog.show()

    def onOpenAnonymiseClicked(self):
        self.dialog = AnonymiseGUI.AnonymiseFaces(app)
        self.dialog.show()

    def adjustScreen(self):
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.8)
            height = int(screenHeight / 2)
        else:
            width = int(screenWidth / 2.22222)
            height = int(screenHeight / 1.95298)
        self.setGeometry(500, 80, width, height)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())
