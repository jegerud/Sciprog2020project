import numpy as np
import matplotlib.pyplot as plt
import imageio
import sys
sys.path.insert(0, '../')
import Source.Eksplisitt as eks
import Source.Grayscale as gray
import Source.ImageView as imv


def Inpaint(file, ret=1, alpha=.25, n=100, colour=True):
    im = imageio.imread(file)
    orig_im = np.copy(im)
    if colour:
        im = im.astype(dtype=float) / 255
        gray_im =np.sum(im.astype(float), 2) / (3 * 255)
        mask = np.zeros(gray_im.shape)
    else:
        im = np.sum(im.astype(float), 2) / (3 * 255)  #gråtone
        mask = np.zeros(im.shape)     #lag maske
    im[im < 0] = 0                                 # klipp til lovlige verdier
    im[im > 1] = 1

    mask[135:140, 250:380] = 1
    mask[250:470, 300:305] = 1
    mask[740:755, 550:700] = 1
    mask = mask.astype(bool)

    im[mask] = 0
    im, im0 = eks.eksplisittInpaint(im, mask)

    if ret == 1:
        return orig_im, im0, im
    elif ret == 2:
        return mask
    else:
        return im