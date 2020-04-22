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
    for i in range(n):
        u[1:-1, 1:-1]+=alpha*(u[:-2, 1:-1]+
                          u[2:, 1:-1]+
                          u[1:-1, :-2]+
                          u[1:-1, 2:]-
                          4*u[1:-1, 1:-1])
        u[:, 0] = u[:, 1]      # Neumann randbetingelse
        u[:, -1] = u[:, -2]    #
        u[0, :] = u[1, :]      #
        u[-1, :] = u[-2 , :]   #
    return u


def eksplisittAnonym(u,u_0, alpha, n):
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
    for i in range(n):
        u[1:-1, 1:-1] += alpha * (u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + u[1:-1, 2:]-4 * u[1:-1, 1:-1]) 
        u[0] = u_0[0]   #Dirichlet randbetingelser
        u[-1] = u_0[-1] #
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
    im0 = np.copy(im)
    im[im < 0] = 0                # klipp til lovlige verdier
    im[im > 1] = 1
    for i in range(25):
        im=eksplisitt(im, n=1)  #løs
        im[np.logical_not(mask)] = im0[np.logical_not(mask)]         #ja
    return im