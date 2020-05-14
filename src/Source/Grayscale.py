import numpy as np
import imageio
from Source.Eksplisitt import finnLaplace
from Source.ImageView import twoImageSetup

def grayscale(file):
    """
    Konverterer bildet til gråtoner

    Parameters
    ---------
    file : path
        Path til bildet som skal konverteres til gråtoner

    Returns
    -------
    Picture:
        Kopi av originalbildet i gråtoner
    """
    picture =  imageio.imread(file)                 # Leser inn bildet
    gray = np.sum(picture.astype(float),2)/(3*255)  # Lager gråtonebilde

    return gray 

def rgb2gray(file):
    """
    Konverterer bildet til gråtoner

    Parameters
    ---------
    file : path
        Path til bildet som skal konverteres til gråtoner

    Returns
    --------
    Picture:
        Kopi av originalbildet i gråtoner
    """
    orig_im = imageio.imread(file)      # Leser inn bildet
    gray_im = grayscale(file)           # Henter enkel gråtoneversjon av bildet
    u0 = np.copy(gray_im)               # Kopierer gråtonebilde over i u0
    orig_im = orig_im.astype(float)/255 # np.array verdier mellom 0 og 1
    
    gradient = abs(finnLaplace(u0))/np.sqrt(3)
    retning = finnLaplace(orig_im[:,:,0] + orig_im[:,:,1] + orig_im[:,:,2])

    alpha = .25
    for i in range(2):                  # Løser diffusjonslikning
        laplace = finnLaplace(u0)
                                        # Løser diffusjonsliknig
        u0[1:-1, 1:-1] += alpha * laplace - retning*gradient
        u0[:, 0] = u0[:, 1]             # Neumann randbetingelser
        u0[:, -1] = u0[:, -2]    
        u0[0, :] = u0[1, :]      
        u0[-1, :] = u0[-2 , :]   
        u0[u0 < 0] = 0                  # Klipper til lovlige verdier
        u0[u0 > 1] = 1
    return u0

def viewGrayImage(image1, image2):
    """
    Viser bildene ved siden av hverandre

    Parameters
    ---------
    image1 : path
             Bildet som skal vises
    image2 : path
             Bildet som skal vises
    Returns
    --------
    Picture:
        Bildene displayet ved siden av hverandre
    """
    twoImageSetup(image1, image2, "Enkel", "Avansert")