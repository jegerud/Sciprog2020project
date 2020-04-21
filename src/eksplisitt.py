import numpy as np
import unittest

def eksplisitt(u, alpha=0.25, h=1, n=1000):
    """
    Løser diffusjonslikningen

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n tider

    Paramters
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
        u[1:-1, 1:-1]+=alpha*laplace(u)
        u[:, 0] = u[:, 1]      # Neumann randbetingelse
        u[:, -1] = u[:, -2]    #
        u[0, :] = u[1, :]      #
        u[-1, :] = u[-2 , :]   #
    return u

def laplace(im):
    """
    Finner og returnerer laplace-operatoren

    Parameters
    ----------
    im : numpy array
         Finn laplacen for arrayen

    Returns
    -------
    Numpy array: 
        Verdier for laplacen
    """

    lap= (im[0:-2, 1:-1] +
            im[2:, 1:-1] +
            im[1:-1, 0:-2] +
            im[1:-1, 2:] -
            4 * im[1:-1, 1:-1])
    return lap

def dirichlet(u,u_0, alpha, h, n):
    """
    Løser diffusjonslikningen

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n tider

    Paramters
    ---------
    u     : func
        Funksjonen som beskriver diffusjonslikningen
    u_0   :func
        Funksjonen som ikke har blitt anvendt
    n     : int
        Antall tidspunkter
    h     : funksjon
          Spesifiseres ut fra problemet
    alpha : float
        dt/dx**2

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


def Inpainting_rgb(im, mask, alpha, n):
    """
    Inpainter et bilde

    Parameters
    ----------
    im   : numpy array
           Bildet som skal inpaintes
           
    mask  : bool-array
            
    alpha : float
           dt/dx**2
    n     : int
           Antall iterasjoner

    Returns
    -------
    Numpy array: 
        Det inpaintede bildet
    """

    im0 = np.copy(im)
    im[im < 0] = 0                # klipp til lovlige verdier
    im[im > 1] = 1
    for i in range(n):
        eksplisitt(im, alpha, 1)
        im[mask] = im0[mask]

    return im

