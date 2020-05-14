import numpy as np
import unittest

def eksplisitt(u, alpha=0.25, h=0, n=1000):
    """
    Løser diffusjonslikningen

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n tider

    Parameters
    ---------
    u : func
        Funksjonen som beskriver diffusjonslikningen
    n : int
        Antall tidspunkter
    h : funksjon
        Spesifiseres ut fra problemet
    alpha : float
        dt/dx**2

    Returns
    -------
    numpy.ndarray:
        Beregnede verdier for u
    """
    for i in range(n):          # Itererer n antall ganger
        u[1:-1, 1:-1]+=alpha*(u[:-2, 1:-1]+ # Løser diffusjonslikning
                          u[2:, 1:-1]+
                          u[1:-1, :-2]+
                          u[1:-1, 2:]-
                          4*u[1:-1, 1:-1])
        u[:, 0] = u[:, 1]       # Neumann randbetingelse
        u[:, -1] = u[:, -2]     
        u[0, :] = u[1, :]      
        u[-1, :] = u[-2 , :]   
    return u

def eksplisittDirichlet(u,u_0, alpha=0.25, n=1000):
    """
    Løser diffusjonslikningen

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n tider

    Parameters
    ---------
    u : func
        Funksjonen som beskriver diffusjonslikningen
    u_0: func
        Original u
    alpha : float
        dt/dx**2
    n : int
        Antall tidspunkter

    Returns
    -------
    numpy.ndarray:
        Beregnede verdier for u
    """
    for i in range(n):  # Itererer n antall ganger 
        u[1:-1, 1:-1] += alpha * (u[:-2, 1:-1] + # Løser diffusjonslikning
                                  u[2:, 1:-1] + 
                                  u[1:-1, :-2] + 
                                  u[1:-1, 2:]- 
                                  4 * u[1:-1, 1:-1]) 
        u[0] = u_0[0]   #Dirichlet randbetingelser
        u[-1] = u_0[-1] 
    return u


def Inpainting_mosaic(im, mask):
    """
    Inpainter et bilde med en maske

    Parameters
    ---------
    im : numpu.ndarray
        Bildet som skal inpaintes
    mask : numpy array
           Masken
    Returns
    -------
    numpy.ndarray:
        Det inpaintede bildet
    """
    im0 = np.copy(im)             # Lager kopi av bilde
    im[im < 0] = 0                # klipp til lovlige verdier
    im[im > 1] = 1
    for i in range(25):           # Itererer 
        im = eksplisitt(im, n=1)  # Løser ved hjelp av eksplisittfunksjon
        im[np.logical_not(mask)] = im0[np.logical_not(mask)] 
    return im

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
    iteration = 20
    delta_t = 1 / iteration
    
    for i in range(iteration):          # Iterer 
        laplace = (image[0:-2, 1:-1] +  # Laplace for u
            image[2:, 1:-1] +
            image[1:-1, 0:-2] +
            image[1:-1, 2:] -
            4 * image[1:-1, 1:-1])
        h = k * delta_t * (image[1:-1, 1:-1] - # Finner h-ledd
                           orig_im[1:-1, 1:-1])
        image[1:-1, 1:-1] += .25 * (laplace - h) # Løser diffusjonslikning
        image[:, 0] = image[:, 1]      # Neumann randbetingelse
        image[:, -1] = image[:, -2]    
        image[0, :] = image[1, :]      
        image[-1, :] = image[-2 , :]   
    image[image < 0] = 0           # klipp til lovlige verdier
    image[image > 1] = 1
    return image

def eksplisittInpaint(image, mask, alpha=.25, n=100):
    """
    Løser diffusjonslikningen

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n tider

    Parameters
    ---------
    u : func
        Funksjonen som beskriver diffusjonslikningen
    n : int
        Antall tidspunkter
    h : funksjon
        Spesifiseres ut fra problemet
    alpha : float
        dt/dx**2

    Returns
    -------
    numpy.ndarray:
        Beregnede verdier for u
    """
    im = image
    im0 = np.copy(im)

    for i in range(n):                              # Iterer
        im[1:-1, 1:-1] += alpha * (im[:-2, 1:-1] +  # Løser diffusjonslikning
                                  im[2:, 1:-1] +
                                  im[1:-1, :-2] +
                                  im[1:-1, 2:] -
                                  4 * im[1:-1, 1:-1])
        im[mask == False] = im0[mask == False]      # Diriclet randbetingelse
    return im

def finnLaplace(u):
    """
    Finner laplacen til en matrise

    Parameters
    ---------
    u : image
        bildet laplacen skal hentes fra

    Returns
    -------
    numpy.ndarray:
        Divergensen til gradienten til u (laplacen)
    """
    laplace=u[0:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, 0:-2] + u[1:-1, 2:] - 4 * u[1:-1, 1:-1]
    return laplace