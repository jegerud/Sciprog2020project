from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import imageio
import Eksplisitt as eks
import ImageView as imv
import unittest

import os
import colour
from colour.plotting import *
from colour_demosaicing import (demosaicing_CFA_Bayer_Menon2007, mosaicing_CFA_Bayer)


def getMosaic(file):
    im = imageio.imread(file)
    im = im.astype(float) / 255

    mosaic = np.zeros(im.shape[:2]) # Alloker plass
    mosaic[ ::2, ::2] = im[ ::2, ::2, 0]   #R
    mosaic[1::2, ::2] = im[1::2, ::2, 1]   #G
    mosaic[ ::2, 1::2] = im[ ::2, 1::2, 1] #G
    mosaic[1::2, 1::2] = im[1::2, 1::2, 2] #B

    return mosaic


def mosaicToRgb(file, view=False):
    im = imageio.imread(file)
    im = im.astype(float) / 255
    
    #lag mosaic
    mosaic = np.zeros(im.shape[:2]) # Alloker plass
    mosaic[ ::2, ::2] = im[ ::2, ::2, 0]   #R
    mosaic[1::2, ::2] = im[1::2, ::2, 1]   #G
    mosaic[ ::2, 1::2] = im[ ::2, 1::2, 1] #G
    mosaic[1::2, 1::2] = im[1::2, 1::2, 2] #B
    
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
    eks.Inpainting_mosaic(im_ed[:,:,0], mask[:,:,0])
    eks.Inpainting_mosaic(im_ed[:,:,1], mask[:,:,1])
    eks.Inpainting_mosaic(im_ed[:,:,2], mask[:,:,2])
    
    if view:
        imv.viewDemosaic(im, mosaic, im_ed, "Demosaicing - Algorithm")
    else:
        return im_ed


def packageDemo(file, view=False):
    original = colour.io.read_image(file)

    mosaic = mosaicing_CFA_Bayer(original)
    new = demosaicing_CFA_Bayer_Menon2007(mosaic)
    new[new < 0] = 0
    new[new > 1] = 1

    if view:
        imv.viewDemosaic(original, mosaic, new, "Demosaicing - Package")
    else:
        return new