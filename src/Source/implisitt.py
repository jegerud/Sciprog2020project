import numpy as np
import Source.ImageView as im
import matplotlib.pyplot as plt
import imageio
import Source.ImageView as im
import Source.Eksplisitt as eks
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve

def implisitt(u, alpha=0.25, h=0, n=1, rgb=True):
    """
    Løser diffusjonslikningen implisitt med sparse-matriser

    Løser du/dt= d**2u/dx**2 +d**2u/dy**2 med n iterasjoner

    Parameters
    ---------
    u : array
        bildet som skal behandles
    n : int
        Antall interasjoner
    h : funksjon
        Spesifiseres ut fra problemet
    alpha : float
        dt/dx**2
    rgb : bool
        er bildet et fargebilde?

    Returns
    -------
    numpy.ndarray:
        Beregnede verdier for u
    """
    #lager diagonalmatrise
    size=u.shape[0]*u.shape[1]

    nupper = np.concatenate((np.zeros(u.shape[1]), -alpha * np.ones(size - u.shape[1])))
    upper = np.concatenate(([0, 0], -alpha * np.ones(size - 2)))
    center = np.concatenate(([1], (1 + 4 * alpha) * np.ones(size - 2), [1]))
    lower = np.concatenate((-alpha * np.ones(size - 2), [0, 0]))
    nlower = np.concatenate((-alpha * np.ones(size - u.shape[1]), np.zeros(u.shape[1])))
    diags = np.array([nupper, upper, center, lower, nlower])
    A = spdiags(diags, [u.shape[1], 1, 0, -1, -u.shape[1]], size, size).tocsc()

    im=np.copy(u)
    if rgb:
        for iterations in range(n):
            for i in range (u.shape[2]):
                im[:,:,i]=spsolve(A,im[:,:,i].flatten()).reshape(u[:,:,i].shape)
                im[:, 0,] = im[:, 1]      # Neumann randbetingelser
                im[:, -1] = im[:, -2]     #
                im[0, :] = im[1, :]       #
                im[-1, :] = im[-2 , :]    #
            
    else:
        for iterations in range(n):
            im=spsolve(A,im.flatten())
            im=im.reshape(u.shape)
            im[:, 0,] = im[:, 1]      # Neumann randbetingelser
            im[:, -1] = im[:, -2]     #
            im[0, :] = im[1, :]       #
            im[-1, :] = im[-2 , :]    #
                
    return im


def viewImplisitt(file):
    """
    Tar et bilde og glatter det med implisitt skjema
    Viser bildene ved siden av hverandre.
    Sammenligner et eksplisitt glattet bilde
    Parameter
    ---------
    file :     Bildefil
               Bilde som skal bli anvendt
    """
    u=imageio.imread(file)
    u = u.astype(float) / 255
    u[u<0]=0
    u[u>1]=1
    copy=np.copy(u)
    eksIm=eks.eksplisittGlatting(u,copy, 3)
    impIm = implisitt(u,n=5, alpha=1,rgb=True)
    
    im.twoImageSetup(eksIm, impIm,'Eksplisitt','Implisitt')