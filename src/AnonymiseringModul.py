import numpy as np
import cv2
import ImageView as iv
import eksplisitt as eks
import matplotlib.pyplot as plt
import sys

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
        blur = eks.eksplisittAnonym(RoI,image[y:y+h, x:x+w], 0.25,250)               
        image[y:y+h, x:x+w] = blur
        
    return len(faces), image