import numpy as np
import matplotlib.pyplot as plt
import imageio
import Eksplisitt as eks
import Grayscale as gray
import ImageView as imv

def Inpaint(file, ret = 1):
    im = imageio.imread(file)
    im = np.sum(im.astype(float), 2) / (3 * 255)  #gråtone
    im0 = np.copy(im)
    im[im < 0] = 0                                 # klipp til lovlige verdier
    im[im > 1] = 1

    mask = np.ones(im.shape)     #lag maske
    mask[350:400 ,450:550] = 0
    mask[500:650 ,300:500] = 0
    mask[200:300 ,700:800] = 0
    mask = mask.astype(bool)
    
    im=eks.eksplisitt(im, n=20)  #løs
    im[mask] = im0[mask]         #ja
    
    if ret == 1:
        return im0, mask, im
    elif ret == 2:
        return mask
    else:
        return im


def Inpaint_rgb(file, ret = 1):
    orig_im = imageio.imread(file)
    im=np.copy(orig_im)
    im = im.astype(dtype=float) / 255
    gray_im =np.sum(im.astype(float), 2) / (3 * 255)  #gråtone trengs for å vise masken
    im0 = np.copy(im)
    im[im < 0] = 0                # klipp til lovlige verdier
    im[im > 1] = 1

    mask = np.ones(gray_im.shape) #lag maske
    mask[350:400 ,450:550] = 0
    mask[500:650 ,300:500] = 0
    mask[200:300 ,700:800] = 0
    mask = mask.astype(bool)      #lag bool-array

    im=eks.eksplisitt(im, n=20)   #løs

    im[mask] = im0[mask]          #ja
    if ret == 1:
        return orig_im, mask, im
    elif ret == 2:
        return mask
    else:
        return im