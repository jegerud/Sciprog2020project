import numpy as np
import imageio

def grayscale(file):
    """
    Konverterer bildet til gråtoner

    Løser 

    Parameters
    ---------
    file : picture
        Bildet som skal konverteres til gråtoner

    Returns
    Picture:
        Kopi av originalbildet i gråtoner
    -------
    """
    picture =  imageio.imread(file)
    gray = np.sum(picture.astype(float),2)/(3*255)

    return gray 

def rgb2gray(file):
    pic =  imageio.imread(file)
    r, g, b = pic[:,:,0], pic[:,:,1], pic[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray