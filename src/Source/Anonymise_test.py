import unittest
from Source.Anonymise import blurFace
from Source.Anonymise import detectFace

lena = '../../hdr-bilder/Faces/lena.png'
team = '../../hdr-bilder/Faces/team.jpg'

class Anonymise_test(unittest.TestCase):
    """
    Tests for the anonymise module
    """
    def faceDetect_test(self):
        """
        test for face detection
        """
        antall, lena_image = detectFace(lena)
        expectedNumber = 1
        self.assertEqual(antall, expectedNumber)
    
    
    