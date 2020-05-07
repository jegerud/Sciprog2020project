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
    """
    Lager gråtonemosaikk av originalbildet

    Paramters
    ---------
    file : text
        Path til bildet det skal lages gråtonemosaikk av
    
    Returns
    -------
    im:
	Gråtonemosaikken
    """
    im = imageio.imread(file)       # Leser bilde
    im = im.astype(float) / 255     # Arrayverdien fra 0 - 1

    mosaic = np.zeros(im.shape[:2]) # Alloker plass
    mosaic[ ::2, ::2] = im[ ::2, ::2, 0]   #R
    mosaic[1::2, ::2] = im[1::2, ::2, 1]   #G
    mosaic[ ::2, 1::2] = im[ ::2, 1::2, 1] #G
    mosaic[1::2, 1::2] = im[1::2, 1::2, 2] #B

    return mosaic


def getMosaicPackage(file):
    """
    Lager gråtonemosaikk med hjelp av bibliotek

    Paramters
    ---------
    file : text
        Path til bildet det skal lages gråtonemosaikk av

    Returns
    -------
    im:
	Gråtonemosaikk
    """
    im = imageio.imread(file)       # Leser bilde
    im = im.astype(float) / 255     # Arrayverdien fra 0 - 1
    return mosaicing_CFA_Bayer(im)  # Henter gråtonemosaikk


def mosaicToRgb(file):
    """
    Lager et RGB-bilde av gråtonemosaikk

    Parameters
    ---------
    file : text
        Path til bildet som det skal gjøres demosaic på

    Returns
    -------
    im:
	Demosaiced bilde
    """
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
    original = colour.io.read_image(file) # Leser bilde
    mosaic = mosaicing_CFA_Bayer(original)# Henter gråtonemosaikk
    new = demosaicing_CFA_Bayer_Menon2007(mosaic)# Gjør demosaicing
    new[new < 0] = 0                # Klipper til lovlige verdier
    new[new > 1] = 1                

    return new