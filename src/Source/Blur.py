import numpy as np
import unittest
import imageio
import Source.Grayscale as gray
import Source.Eksplisitt as eks
import Source.ImageView as imv

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


def glatting(file, k=1.3):
    """
    Tar et bilde og glatter det. Displayer det såi farger og i gråskala
    Paramters
    ---------
    file : bildet
           Bildet som skal glattes
    k    : int
           Styrer hvor mye bildet skal glattes
    Returns
    -------
    im:
	Et glattet bilde
    """
    orig_im = imageio.imread(file).astype(float)/255              #Originalbilde
    im = np.copy(orig_im)
    orig_gray_im =  gray.rgb2gray(file)
    gray_im =  gray.rgb2gray(file)
    
    im = im + .05 * np.random.randn(* np.shape(im))                #legger på tilfeldig støy
    gray_im = gray_im + .05 * np.random.randn(* np.shape(gray_im)) #legger på tilfeldig støy
    
    im = eks.eksplisittGlatting(im, orig_im, k)
    gray_im = eks.eksplisittGlatting(gray_im, orig_gray_im, k)
    imv.view(orig_im, im, orig_gray_im, gray_im, "Glatting") 