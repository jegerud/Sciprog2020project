from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('mainWindow.ui', self)

        self.openGlatting.clicked.connect(self.onOpenGlattingClicked)
        self.dialog = Glatting()
    
    def onOpenGlattingClicked(self):
        self.dialog.show()

class Glatting(QMainWindow):
    def __init__(self):
        super(Glatting, self).__init__()
        uic.loadUi('glatting.ui', self)
        self.adjuster.clicked.connect(self.showAdjuster)
        self.balls.clicked.connect(self.showBalls)
        self.fog.clicked.connect(self.showFog)
        self.garden.clicked.connect(self.showGarden)
        self.mountains.clicked.connect(self.showMountains)
        self.ocean.clicked.connect(self.showOcean)
        self.stillife.clicked.connect(self.showStillife)
        self.trees.clicked.connect(self.showTrees)
        self.glattingKode.clicked.connect(self.showCode)

    def showAdjuster(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/Adjuster/Adjuster_00032.png"))

    def showBalls(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/Balls/Balls_00032.png"))

    def showFog(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/Fog/Fog_00128.png"))

    def showGarden(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/Garden/Garden_00004.png"))

    def showMountains(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/MtTamNorth/MtTamNorth_00004.png"))

    def showOcean(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/Ocean/Ocean_00256.png"))
    
    def showStillife(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/StillLife/StillLife_01024.png"))

    def showTrees(self):
        self.glattingBilde.setPixmap(QtGui.QPixmap("../../hdr-bilder/Tree/Tree_00064.png"))
    
    def showCode(self):
        code = QPlainTextEdit()
        text = open('codes/glatting.txt').read()
        title = "Glatting kode"
        code.setPlainText(text)
        self.dialog = ShowCode(text, title)
        self.dialog.show()

class ShowCode(QDialog):
    def __init__(self, text, title, parent=None):
        super(ShowCode, self).__init__(parent)
        self.setWindowTitle(title)
        self.setGeometry(500, 80, 480, 600)
        codeLabel = QtWidgets.QLabel(self)
        codeLabel.setText(text)
        codeLabel.move(10, 20)
        codeLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())