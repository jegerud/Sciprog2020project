import numpy as np
import unittest
import imageio
from Source.Eksplisitt import eksplisitt
from Source.Grayscale import rgb2gray

def contrastEnhanceBW(file, k):
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
    u = rgb2gray(file)
    u0 = 0.25 * (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + 
                u[1:-1, 2:] - 4 * u[1:-1, 1:-1])

    for i in range(30):
        u[1:-1, 1:-1] += (0.25 * (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + 
                                u[1:-1, 2:] - 4 * u[1:-1, 1:-1]) - k * u0)
        u[:, 0] = u[:, 1]      # Neumann randbetingelse
        u[:, -1] = u[:, -2]    #
        u[0, :] = u[1, :]      #
        u[-1, :] = u[-2 , :]   #
        u[u < 0] = 0           # klipp til lovlige verdier
        u[u > 1] = 1
    return u



def contrastEnhance(file, k):
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
    u = imageio.imread(file) / 255
    u0 = np.copy(u[1:-1, 1:-1, :])
    u0[:,:,0] = 0.25 * (u[:-2, 1:-1, 0] + u[2:, 1:-1, 0] + u[1:-1, :-2, 0] + 
                    u[1:-1, 2:, 0] - 4 * u[1:-1, 1:-1, 0])  
    u0[:,:,1] = 0.25 * (u[:-2, 1:-1, 1] + u[2:, 1:-1, 1] + u[1:-1, :-2, 1] + 
                    u[1:-1, 2:, 1] - 4 * u[1:-1, 1:-1, 1])  
    u0[:,:,2] = 0.25 * (u[:-2, 1:-1, 2] + u[2:, 1:-1, 2] + u[1:-1, :-2, 2] + 
                    u[1:-1, 2:, 2] - 4 * u[1:-1, 1:-1, 2])  

    for i in range(30):
        u[1:-1, 1:-1, 0] += (0.25 * (u[:-2, 1:-1, 0] + u[2:, 1:-1, 0] + 
                            u[1:-1, :-2, 0] + u[1:-1, 2:, 0] - 
                            4 * u[1:-1, 1:-1, 0]) - k * u0[:,:, 0])
        u[1:-1, 1:-1, 1] += (0.25 * (u[:-2, 1:-1, 1] + u[2:, 1:-1, 1] + 
                            u[1:-1, :-2, 1] + u[1:-1, 2:, 1] - 
                            4 * u[1:-1, 1:-1, 1]) - k * u0[:,:, 1])
        u[1:-1, 1:-1, 2] += (0.25 * (u[:-2, 1:-1, 2] + u[2:, 1:-1, 2] + 
                            u[1:-1, :-2, 2] + u[1:-1, 2:, 2] - 
                            4 * u[1:-1, 1:-1, 2]) - k * u0[:,:, 2])
        u[:, 0] = u[:, 1]      # Neumann randbetingelse
        u[:, -1] = u[:, -2]    #
        u[0, :] = u[1, :]      #
        u[-1, :] = u[-2 , :]   #
    u[u < 0] = 0           # klipp til lovlige verdier
    u[u > 1] = 1
    return u