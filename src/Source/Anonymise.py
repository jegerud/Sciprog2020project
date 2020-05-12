import numpy as np
import cv2
import matplotlib.pyplot as plt
import Source.Eksplisitt as eks
from Source.ImageView import singleView

def blurFace(file, scaleFactor = 1.2, minNeighbors = 5):
    """
    Oppdager et ansikt vendt mot kamera
   
    Parameters + some explanation
    ---------
    file         : Bildefil
                    Pathen til filen der original bildet befinner seg uten andvending
    scaleFactor  : int
                    Kompenserer i tilfelle noen ansikter er nærmere kamera enn andre
    minNeighbors : int
                    spesifiserer antall naboer en rektangel bør ha for å bli kalt et "ansikt"
    title        : text
                    Tittelen på bildet som er anvendt

    Returns
    -------
    len(faces):
        Antall ansikter
    image:
        Bilde med anonymiserte ansikter
    """
    image = cv2.imread(file)                                # leser inn bildet
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)          # konverterer til RGB
    
    face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml') # importerer haarscade biblioteket
    faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors, minSize = (30,30)) # Gjenkjenner ansikter
    for (x,y,w,h) in faces:
        RoI = image[y:y+h, x:x+w]                           # Region of Interest --> ansiktet
        RoI = RoI.astype(dtype = float)
        blur = eks.eksplisittDirichlet(RoI,image[y:y+h, x:x+w], 0.25,250)               
        image[y:y+h, x:x+w] = blur
        
    return len(faces), image


def detectFace(file, scaleFactor = 1.2, minNeighbours = 5):
    """
    Oppdager et ansikt vendt mot kamera
   
    Parameters
    ---------
    file        : Bildefil
                  Pathen til filen der original bildet befinner seg uten andvending
    scaleFactor : int
                  Kompenserer i tilfelle noen ansikter er nærmere kamera enn andre
    minNeighbors : int
                  spesifiserer antall naboer en rektangel bør ha for å bli kalt et "ansikt"
    title       : text
                  Tittelen på bildet som er anvendt

    Returns
    -------
    len(faces):
        Antall ansikter
    image:
        Bilde med markerte ansikter
    """
    image = cv2.imread(file)                        # Leser inn bilde
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konverterer til RGB
    
    face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')# importerer haarscade biblioteket
    faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbours, minSize = (30,30))# Gjenkjenner ansikter
    faces_rects = face_cascade.detectMultiScale(image, scaleFactor, minNeighbours)        # Antall ansikter og markere

    for (x,y,w,h) in faces_rects:                                   # For hvert oppdagede ansikt
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)    # Lager rektangel rundt ansikt

    return len(faces), image

def detect_anonymise(path):
    antall, image = detectFace(path)
    antall, blur = blurFace(path)
    print(antall, "ansikt er registrert")
    singleView(image)
    singleView(blur)