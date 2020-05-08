import numpy as np
import unittest
import imageio
from Source.Eksplisitt import eksplisitt
from Source.Grayscale import rgb2gray

def contrastEnhanceBW(file, k):
    """
    Øker kontrasten i et gråtonebilde

    Parameters
    ---------
    file : Path 
        Path til bilde som skal kontrastforsterkes
    k : konstant
        Styrer hvor mye bildet skal glattes
    Returns
    -------
    im:
	    Kontrastforsterket bilde i gråtoner
    """
    u = rgb2gray(file)         # Henter gråtoneversjon av bildet
    u0 = 0.25 * (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + # Laplace av u0
                u[1:-1, 2:] - 4 * u[1:-1, 1:-1])

    for i in range(30):        # Løser diffusjonslikningen
        u[1:-1, 1:-1] += (0.25 * (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + 
                                u[1:-1, 2:] - 4 * u[1:-1, 1:-1]) - k * u0)
        u[:, 0] = u[:, 1]      # Neumann randbetingelse
        u[:, -1] = u[:, -2]    
        u[0, :] = u[1, :]      
        u[-1, :] = u[-2 , :]   
        u[u < 0] = 0           # klipp til lovlige verdier
        u[u > 1] = 1
    return u

def contrastEnhance(file, k):
    """
    Øker kontrasten i et bilde

    Parameters
    ---------
    file : Path 
        Path til bilde som skal kontrastforsterkes
    k : konstant
        Styrer hvor mye bildet skal glattes
    Returns
    -------
    im:
	    Kontrastforsterket bilde
    """
    u = imageio.imread(file) / 255  # np.array verdier mellom 0 og 1
    u0 = np.copy(u[1:-1, 1:-1, :])  # Kopierer over i u0

                                    # Laplace av hver fargekanal
    u0[:,:,0] = 0.25 * (u[:-2, 1:-1, 0] + u[2:, 1:-1, 0] + u[1:-1, :-2, 0] + 
                    u[1:-1, 2:, 0] - 4 * u[1:-1, 1:-1, 0])  # R
    u0[:,:,1] = 0.25 * (u[:-2, 1:-1, 1] + u[2:, 1:-1, 1] + u[1:-1, :-2, 1] + 
                    u[1:-1, 2:, 1] - 4 * u[1:-1, 1:-1, 1])  # G
    u0[:,:,2] = 0.25 * (u[:-2, 1:-1, 2] + u[2:, 1:-1, 2] + u[1:-1, :-2, 2] + 
                    u[1:-1, 2:, 2] - 4 * u[1:-1, 1:-1, 2])  # B

    for i in range(30):             # Løser diffusjonslikningen i hver fargekanal
        u[1:-1, 1:-1, 0] += (0.25 * (u[:-2, 1:-1, 0] + u[2:, 1:-1, 0] + 
                            u[1:-1, :-2, 0] + u[1:-1, 2:, 0] - 
                            4 * u[1:-1, 1:-1, 0]) - k * u0[:,:, 0]) # R
        u[1:-1, 1:-1, 1] += (0.25 * (u[:-2, 1:-1, 1] + u[2:, 1:-1, 1] + 
                            u[1:-1, :-2, 1] + u[1:-1, 2:, 1] - 
                            4 * u[1:-1, 1:-1, 1]) - k * u0[:,:, 1]) # G
        u[1:-1, 1:-1, 2] += (0.25 * (u[:-2, 1:-1, 2] + u[2:, 1:-1, 2] + 
                            u[1:-1, :-2, 2] + u[1:-1, 2:, 2] - 
                            4 * u[1:-1, 1:-1, 2]) - k * u0[:,:, 2]) # B
        u[:, 0] = u[:, 1]      # Neumann randbetingelse
        u[:, -1] = u[:, -2]    
        u[0, :] = u[1, :]      
        u[-1, :] = u[-2 , :]   
    u[u < 0] = 0           # klipp til lovlige verdier
    u[u > 1] = 1
    return u