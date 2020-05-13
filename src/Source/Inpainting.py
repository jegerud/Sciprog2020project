import numpy as np
import matplotlib.pyplot as plt
import imageio
from Source.ImageView import threeImageSetup
from Source.Eksplisitt import eksplisittInpaint
from Source.Grayscale import grayscale

def Inpaint(file, ret=1, colour=True):
    """
    Fyller inn mangelnde informasjon der dette mangler

    Parameters
    ---------
    file : text
        Path til bildet som det skal gjøres demosaic på
    ret : int
        Bestemmer hvor mye som skal returnes
    colour : Bool
        Sier om bildet er gråtone eller farge

    Returns
    -------
    im:
	    Demosaiced bilde
    im0:
        Bilde med maske
    orig_im:
        Originalbildet
    """ 
    im = imageio.imread(file)           # Leser inn bilde
    orig_im = np.copy(im)               # Lagrer originalversjonen
    if colour:                          # Hvis farger
        im = im.astype(dtype=float) / 255   # np.array verdier mellom 0 og 1
        gray_im = grayscale(file)       # Henter en gråtoneversjon til bruk i maske
        mask = np.zeros(gray_im.shape)  # Lager en numpyarray til masken
    else:
        im = grayscale(file)            # Henter gråtoneversjon gråtone
        mask = np.zeros(im.shape)       # Lager en numpyarray til masken
    im[im < 0] = 0                      # Klipper til lovlige verdier
    im[im > 1] = 1

    mask[135:140, 250:380] = 1          # Bestemmer hvor informasjon skal mangle
    mask[250:470, 300:305] = 1
    mask[740:755, 550:700] = 1
    mask = mask.astype(bool)

    im[mask] = 0                        # Fjerner informasjon i aktuelle områder
    im, im0 = eksplisittInpaint(im, mask)# Fyller inn informasjon

    if ret == 1:                        
        return orig_im, im0, im         
    elif ret == 2:
        return im0
    else:
        return im
    
def viewInpaint(original, mask, ny, text, rgb):
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