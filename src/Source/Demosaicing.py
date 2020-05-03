from __future__ import division
from colour.plotting import *
from colour_demosaicing import (demosaicing_CFA_Bayer_Menon2007, mosaicing_CFA_Bayer)
import colour
import numpy as np
import matplotlib.pyplot as plt
import imageio
import unittest
import os
from Source.Eksplisitt import Inpainting_mosaic


def getMosaic(file):
    im = imageio.imread(file)
    im = im.astype(float) / 255

    mosaic = np.zeros(im.shape[:2]) # Alloker plass
    mosaic[ ::2, ::2] = im[ ::2, ::2, 0]   #R
    mosaic[1::2, ::2] = im[1::2, ::2, 1]   #G
    mosaic[ ::2, 1::2] = im[ ::2, 1::2, 1] #G
    mosaic[1::2, 1::2] = im[1::2, 1::2, 2] #B

    return mosaic


def getMosaicPackage(file):
    im = imageio.imread(file)
    im = im.astype(float) / 255
    return mosaicing_CFA_Bayer(im) 


def mosaicToRgb(file):
    im = imageio.imread(file)
    im = im.astype(float) / 255
    mosaic = getMosaic(file)
    
    #fyller inn i fargekanalene fra mosaic
    im_ed= np.zeros(im.shape)
    im_ed[ ::2, ::2, 0]=mosaic[ ::2, ::2]  #R
    im_ed[1::2, ::2, 1]=mosaic[1::2, ::2]  #G
    im_ed[ ::2, 1::2, 1]=mosaic[ ::2, 1::2]#G
    im_ed[1::2, 1::2, 2]=mosaic[1::2, 1::2]#B

    #lager maske for alle fargekanalene
    mask = np.ones(im_ed.shape)
    mask[ ::2, ::2, 0]=0  #R
    mask[1::2, ::2, 1]=0  #G
    mask[ ::2, 1::2, 1]=0 #G
    mask[1::2, 1::2, 2]=0 #B
    mask=mask.astype(bool)#gjør om til bool-array
    
    #inpainter hver av fargekanalene
    Inpainting_mosaic(im_ed[:,:,0], mask[:,:,0])
    Inpainting_mosaic(im_ed[:,:,1], mask[:,:,1])
    Inpainting_mosaic(im_ed[:,:,2], mask[:,:,2])

    return im_ed


def mosaicToRgbPackage(file):
    original = colour.io.read_image(file)
    mosaic = mosaicing_CFA_Bayer(original)
    new = demosaicing_CFA_Bayer_Menon2007(mosaic)
    new[new < 0] = 0
    new[new > 1] = 1

    return new