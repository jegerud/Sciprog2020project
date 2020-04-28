import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../')
import Source.ImageView as iv
import Source.Eksplisitt as eks

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
    """
    image = cv2.imread(file) #leser inn bildet
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #importerer haarscade biblioteket
    faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors, minSize = (30,30))
    for (x,y,w,h) in faces:
        RoI = image[y:y+h, x:x+w]                          #Region of Interest --> ansiktet
        RoI = RoI.astype(dtype = float)
        blur = eks.eksplisittDirichlet(RoI,image[y:y+h, x:x+w], 0.25,250)               
        image[y:y+h, x:x+w] = blur
        
    return len(faces), image


def detectFace(file, scaleFactor = 1.2, minNeighbors = 5):
    """
    Oppdager et ansikt vendt mot kamera
   
    Parameters
    ---------
    file        : Bildefil
                  Pathen til filen der original bildet befinner seg uten andvending
    scaleFactor : int
                  Kompenserer i tilfelle noen ansikter er nærmere kamera enn andre
    ny          : int
                  spesifiserer antall naboer en rektangel bør ha for å bli kalt et "ansikt"
    title       : text
                  Tittelen på bildet som er anvendt
    """
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #importerer haarscade biblioteket
    faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors, minSize = (30,30))
    faces_rects = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors)
    
    for (x,y,w,h) in faces_rects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return len(faces), image