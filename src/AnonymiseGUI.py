from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from Source.Grayscale import rgb2gray
from Source.Anonymise import blurFace, detectFace
from FunctionGUI import ShowCode, saveAnonymiseImage
from imagewidget import imagewidget

class AnonymiseFaces(QMainWindow):
    """
    QMainWindow som representerer anonymiseringsvindu
    """
    def __init__(self, app):
        """
        Initialiserer UI
        """
        super(AnonymiseFaces, self).__init__()
        uic.loadUi('anonymise.ui', self)
        self.setWindowIcon(QtGui.QIcon('Resources/logo.png'))
        self.setWindowTitle('Anonymisering')
        self.adjustScreen(app)
        self.number = 0
        self.imgCouple = imageio.imread(self.getPath(1))
        self.imgGroup1 = imageio.imread(self.getPath(2))
        self.imgGroup2 = imageio.imread(self.getPath(3))
        self.imgGroup3 = imageio.imread(self.getPath(4))
        self.imgMusic = imageio.imread(self.getPath(5))
        self.imgFamily = imageio.imread(self.getPath(6))
        self.imgBusiness = imageio.imread(self.getPath(7))
        self.setImage(1)
        self.couple.clicked.connect(partial(self.setImage, 1))
        self.group1.clicked.connect(partial(self.setImage, 2))
        self.group2.clicked.connect(partial(self.setImage, 3))
        self.group3.clicked.connect(partial(self.setImage, 4))
        self.music.clicked.connect(partial(self.setImage, 5))
        self.family.clicked.connect(partial(self.setImage, 6))
        self.business.clicked.connect(partial(self.setImage, 7))
        self.anonymousCode.clicked.connect(self.showCode)
        self.anonymousOriginal.clicked.connect(self.setOriginal)
        self.anonymousFindFaces.clicked.connect(self.detectFaces)
        self.anonymousAnonymise.clicked.connect(self.anonymiseFaces)
        self.save.clicked.connect(partial(self.saveImage))
        self.save.setShortcut("Ctrl+S")
    
    def setImage(self, nr, colour=True):
        """
        Setter nytt bilde og oppdaterer nødvendige variabler

        Parametre:
        ---------
        nr  : int
            Hvilket nummer bildet tilhører
        colour: bool
            Fargebilde eller ikke
        """
        image = imageio.imread(self.getPath(nr))
        self.showImage(image, colour)
        self.number = nr
        self.setSpinboxValues()
        self.updateCount(0)
    
    def showCode(self):
        """
        Viser nytt vindu med aktuell kode
        """
        code = QPlainTextEdit()
        text = open('codes/anonymisering.txt').read()
        title = "Anonymisering - Kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title, 650, 900)
        self.dialog.show()

    def setOriginal(self):
        """
        Fjerner alle endringer på bilde og viser originalversjonen
        """
        image = imageio.imread(self.getPath(self.number))
        self.showImage(image)
        self.setSpinboxValues()
        self.updateCount(0)

    def detectFaces(self):
        """
        Markerer ansiktene på bildet
        Oppdaterer antall ansikter på bildet
        """
        minNeighbours = self.minNeighbours.value()
        scaleFactor = self.scaleFactor.value()
        count, img = detectFace(self.getPath(self.number), scaleFactor, minNeighbours)
        self.updateCount(count)
        self.showImage(img)

    def anonymiseFaces(self):
        """
        Anonymiserer ansiktene på bildet
        Oppdaterer antall ansikter på bildet
        """
        minNeighbours = self.minNeighbours.value()
        scaleFactor = self.scaleFactor.value()
        count, img = blurFace(self.getPath(self.number), scaleFactor, minNeighbours)
        self.updateCount(count)
        self.showImage(img)

    def showImage(self, image, colour=True):
        """
        Oppdaterer aktuelt bilde og viser dette

        Parametre:
        ---------
        image: np.array
            Bildet som skal vises
        colour: bool
            Fargebilde eller ikke
        """
        if self.number == 1: self.imgCouple = image.copy()
        elif self.number == 2: self.imgGroup1 = image.copy()
        elif self.number == 3: self.imgGroup2 = image.copy()
        elif self.number == 4: 
            self.imgGroup3 = image.copy()
            colour=False
        elif self.number == 5: self.imgMusic = image.copy()
        elif self.number == 6: self.imgFamily = image.copy()
        elif self.number == 7: self.imgBusiness = image.copy()
        if colour:
            self.imagewidget.showImage(image)
        else:
            self.imagewidget.showImage(image, False)

    def updateCount(self, count):
        """
        Oppdaterer antallet facecount med antall ansikter

        Parametre:
        ---------
        count:
            Antall ansikter
        """
        self.faceCount.setText(str(count))

    def saveImage(self):
        """
        Lagrer det bildet som vises i bilderammen
        """
        if self.number == 1: saveAnonymiseImage(self.imgCouple)
        elif self.number == 2: saveAnonymiseImage(self.imgGroup1)
        elif self.number == 3: saveAnonymiseImage(self.imgGroup2)
        elif self.number == 4: saveAnonymiseImage(self.imgGroup3)
        elif self.number == 5: saveAnonymiseImage(self.imgMusic)
        elif self.number == 6: saveAnonymiseImage(self.imgFamily)
        elif self.number == 7: saveAnonymiseImage(self.imgBusiness)

    def getPath(self, nr):
        """
        Returnerer filsti til bildet som vises i bilderammen

        Parametre:
        ----------
        nr  : int
            Nummeret til bildet som vises
        """
        if nr == 1: return "../hdr-bilder/Faces/couple.jpg"
        elif nr == 2: return "../hdr-bilder/Faces/group1.jpg"
        elif nr == 3: return "../hdr-bilder/Faces/group2.jpg"
        elif nr == 4: return "../hdr-bilder/Faces/science.jpg"
        elif nr == 5: return "../hdr-bilder/Faces/music.jpg"
        elif nr == 6: return "../hdr-bilder/Faces/family.jpg"
        elif nr == 7: return "../hdr-bilder/Faces/business.jpg"
    
    def setSpinboxValues(self):
        """
        Oppdaterer valueBoxene etter hvilket bilde som skal vises
        """
        if self.number == 1: neigh, scale = 5, 1.200
        elif self.number == 2: neigh, scale = 5, 1.200
        elif self.number == 3: neigh, scale = 8, 1.100
        elif self.number == 4: neigh, scale = 3, 1.194
        elif self.number == 5: neigh, scale = 5, 1.200
        elif self.number == 6: neigh, scale = 5, 1.200
        elif self.number == 7: neigh, scale = 7, 1.225
        self.minNeighbours.setValue(neigh)
        self.scaleFactor.setValue(scale)

    def adjustScreen(self, app):
        """
        Justerer appvinduet basert på skjermens dimensjon

        Parametre:
        ---------
        app : QApplication
            Gir tilgang til skjermens dimensjoner
        """
        screenWidth = app.primaryScreen().size().width()
        screenHeight = app.primaryScreen().size().height()
        dimension = screenWidth/screenHeight
        if dimension == 1.5:
            width = int(screenWidth / 1.75)
            height = int(screenHeight / 2.25)
        else:
            width = int(screenWidth / 2.25)
            height = int(screenHeight / 2.4)
        self.setGeometry(520, 100, width, height)