import numpy as np
import unittest

def eksplisitt(u, alpha=0.25, h=0, n=1000):
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