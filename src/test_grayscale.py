import unittest
import imageio
import Source.Grayscale as gray

file = '../hdr-bilder/Balls/Balls_00016.png'

class test_grayscale(unittest.TestCase):
    def test_isgray(self):
        grayImage = gray.rgb2gray(file)
        shape = (len(grayImage.shape))
       
        self.assertLess(shape,3)
        
    def test_is_not_gray(self):
        image = imageio.imread(file)
        shape = (len(image.shape))
        
        self.assertEqual(shape,3)
        