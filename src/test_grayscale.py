import unittest
import imageio
import Source.Grayscale as gray

file = '../hdr-bilder/Balls/Balls_00016.png'

class test_grayscale(unittest.TestCase):
    """
    Tests for the grayscale module
    """
    def test_is_gray(self):
        """
        Test for if an image is grayscale 
        """
        grayImage = gray.rgb2gray(file)
        shape = (len(grayImage.shape))
       
        self.assertLess(shape,3)
        
    def test_is_not_gray(self):
        """
        Test for if an image is not grayscale 
        """
        image = imageio.imread(file)
        shape = (len(image.shape))
        
        self.assertEqual(shape,3)
        