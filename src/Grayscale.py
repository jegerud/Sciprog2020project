import numpy as np
import imageio

def grayscale(file):
    """
    Konverterer bildet til gråtoner

    Løser 

    Parameters
    ---------
    file : picture
        Bildet som skal konverteres til gråtoner

    Returns
    Picture:
        Kopi av originalbildet i gråtoner
    -------
    """
    picture =  imageio.imread(file)
    gray = np.sum(picture.astype(float),2)/(3*255)

    return gray 

def rgb2gray(file):
    """
    Konverterer bildet til gråtoner

    Løser de likningen med de ulike fargekanalene

    Parameters
    ---------
    file : picture
        Bildet som skal konverteres til gråtoner

    Returns
    Picture:
        Kopi av originalbildet i gråtoner
    -------
    """
    orig_im = imageio.imread(file)
    gray_im = grayscale(file)
    u0 = np.copy(gray_im)
    orig_im = orig_im.astype(float)/255

    dudx = np.zeros(gray_im.shape)
    dudy = np.zeros(gray_im.shape)
    dudx[1:-1, 1:-1] = u0[2:, 1:-1]-u0[1:-1, 1:-1]
    dudy[1:-1, 1:-1] = u0[1:-1, 2:]-u0[1:-1, 1:-1]
    gradient = dudx+dudy
    g = abs(gradient)/np.sqrt(3)
    retning = gradient*(orig_im[:,:,0] + orig_im[:,:,1] + orig_im[:,:,2])

    alpha = .25
    for i in range(2):
        laplace = (u0[0:-2, 1:-1] +
                   u0[2:, 1:-1] +
                   u0[1:-1, 0:-2] +
                   u0[1:-1, 2:] -
                   4 * u0[1:-1, 1:-1])
        u0[1:-1, 1:-1] += alpha * laplace - retning[1:-1, 1:-1]*g[1:-1, 1:-1]
        u0[:, 0] = u0[:, 1]      # Neumann randbetingelser
        u0[:, -1] = u0[:, -2]    
        u0[0, :] = u0[1, :]      
        u0[-1, :] = u0[-2 , :]   
        u0[u0 < 0] = 0
        u0[u0 > 1] = 1
    return u0