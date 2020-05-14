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
import FunctionGUI
import sys
import matplotlib as plt

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Home(QMainWindow):
    """
    QMainWindow som representerer hjemskjermen til applikasjonen
    """
    def __init__(self):
        """
        Initialiserer UI
        """
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
        self.about.clicked.connect(self.onAboutClicked)

    def onOpenBlurClicked(self):
        """
        Åpner vinduet til glatting
        """
        self.dialog = BlurGUI.Blur(app)
        self.dialog.show()

    def onOpenInpaintingClicked(self):
        """
        Åpner vinduet til inpainting
        """
        self.dialog = InpaintingGUI.Inpainting(app)
        self.dialog.show()

    def onOpenContrastClicked(self):
        """
        Åpner vinduet til kontrastforsterkning
        """
        self.dialog = ContrastEnhancementGUI.ContrastEnhancement(app)
        self.dialog.show()

    def onOpenDemosaicingClicked(self):
        """
        Åpner vinduet til demosaicing
        """
        self.dialog = DemosaicingGUI.Demosaic(app)
        self.dialog.show()

    def onOpenSeamlessClicked(self):
        """
        Åpner vinduet til sømløs kloning
        """
        self.dialog = SeamlessGUI.Seamless(app)
        self.dialog.show()
    
    def onOpenGrayscaleClicked(self):
        """
        Åpner vinduet til konvertering til gråtone
        """
        self.dialog = ConvertGrayscaleGUI.GrayscaleConvert(app)
        self.dialog.show()

    def onOpenAnonymiseClicked(self):
        """
        Åpner vinduet til anonymisering
        """
        self.dialog = AnonymiseGUI.AnonymiseFaces(app)
        self.dialog.show()

    def onAboutClicked(self):
        """
        Åpner vinduet til Om oss
        """
        self.dialog = FunctionGUI.ShowAbout(500, 550)
        self.dialog.show()

    def adjustScreen(self):
        """
        Justerer vinduet basert på skjermens dimensjon
        """
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 2.5)
            height = int(screenHeight / 2.25)
        else:
            width = int(screenWidth / 2.75)
            height = int(screenHeight / 2.1)
        self.setGeometry(500, 100, width, height)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())