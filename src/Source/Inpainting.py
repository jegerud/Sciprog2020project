import numpy as np
import matplotlib.pyplot as plt
import imageio
from Source.ImageView import threeImageSetup
from Source.Eksplisitt import eksplisittInpaint
from Source.Grayscale import grayscale

def Inpaint(file, colour=True):
    """
    Fyller inn mangelnde informasjon der dette mangler

    Parameters
    ---------
    file : text
        Path til bildet som det skal gjøres demosaic på
    colour : Bool
        Sier om bildet er gråtone eller farge

    Returns
    -------
    im:
	    Inpaintet bilde
    """
    if colour:
        im = imageio.imread(file)           # Leser inn bilde
        im = im.astype(dtype=float) / 255   # np.array verdier mellom 0 og 1
    else:
        im = grayscale(file)
    mask = getMask(file)
    im[mask] = 0                        # Fjerner informasjon i aktuelle områder
    im = eksplisittInpaint(im, mask)    # Fyller inn informasjon
    return im                           

def maskImage(file, colour=True):
    """
    Fyller inn mangelnde informasjon der dette mangler

    Parameters
    ---------
    file : text
        Path til bildet som det skal gjøres demosaic på

    Returns
    -------
    im:
        Bilde med maske
    """ 
    if colour:
        im = imageio.imread(file)           # Leser inn bilde
        im = im.astype(dtype=float) / 255   # np.array verdier mellom 0 og 1
    else:
        im = grayscale(file)
    mask = getMask(file)
    im[mask] = 0                        # Fjerner informasjon i aktuelle områder
    return im

def getMask(file):
    """
    Fyller inn mangelnde informasjon der dette mangler

    Parameters
    ---------
    file : text
        Path til bildet som det skal lages maske til

    Returns
    -------
    bool array:
        mask
    """ 
    gray_im = grayscale(file)       # Henter en gråtoneversjon til bruk i maske
    mask = np.zeros(gray_im.shape)  # Lager en numpyarray til masken
    mask[135:140, 250:380] = 1      # Bestemmer hvor informasjon skal mangle
    mask[250:470, 300:305] = 1
    mask[740:755, 550:700] = 1
    mask = mask.astype(bool)
    return mask

def viewInpaint(original, mask, ny, text, rgb=True):
    """
    Viser bildene ved siden av hverandre.
    
    Original, masken og inpainted

    Parameters
    ---------
    original : Bildefil
               Pathen til filen der original bildet befinner seg uten andvending
    mask       : Bildefil
               Masken til bildet
    ny       : Bildefil
               Bildet som har blitt anvendt
    text     : text
               Tittelen på bildet som er anvendt
    rgb      : bool
               Fargebilde/gråtone
    
    """
    threeImageSetup(original, mask, ny,'Originalbilde','Mask',text)