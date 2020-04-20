import numpy as np
import unittest

def eksplisittGlatting(im, orig_im, k):
    """
    Løser diffusjonslikningen

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n tider

    Paramters
    ---------
    im : bildet
        Bildet som skal glattes
    orig_im : originalt bilde
        Bild som ikke endres på
    k : konstant
        Styrer hvor mye bildet skal glattes
    Returns
    -------
    im:
	Et glattet bilde
    """
    image = im
    iteration = 30
    delta_t = 1 / iteration
    
    for i in range(iteration):
        laplace = (image[0:-2, 1:-1] +
            image[2:, 1:-1] +
            image[1:-1, 0:-2] +
            image[1:-1, 2:] -
            4 * image[1:-1, 1:-1])
        h = k*delta_t*(image[1:-1, 1:-1] - orig_im[1:-1, 1:-1])
        image[1:-1, 1:-1] += .25 * (laplace - h)
        image[:, 0] = image[:, 1]      # Neumann randbetingelse
        image[:, -1] = image[:, -2]    
        image[0, :] = image[1, :]      
        image[-1, :] = image[-2 , :]   
        image[image < 0] = 0           # klipp til lovlige verdier
        im[im > 1] = 1
    return im