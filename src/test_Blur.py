import unittest
import cv2
import imageio
import Source.Eksplisitt as eks
import Source.Grayscale as gray
import numpy as np
import Source.Blur

Tree   = '../hdr-bilder/Tree/Tree_00032.png'
blur_threshold = 0.01
k = 1

def variance_of_Laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()              

class test_Anon(unittest.TestCase):
    """
    Tests for blur module
    """
    def test_blurred(self):            
        orig_im = imageio.imread(Tree).astype(float)/255
        copy_orig_im =  np.copy(orig_im)
        blur_im = eks.eksplisittGlatting(copy_orig_im, orig_im, 1.5)
        vl = variance_of_Laplacian(blur_im)
        if vl < blur_threshold:
            print("First Image is blurry")
        self.assertLess(vl, blur_threshold)
        
    def test_notblurred(self):
        orig_im = imageio.imread(Tree).astype(float)/255 
        vl = variance_of_Laplacian(orig_im)
        if vl > blur_threshold:
            print("Second Image is not blurry")
        self.assertGreater(vl,blur_threshold) 
        