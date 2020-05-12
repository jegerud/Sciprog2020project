import unittest
from Source.Anonymise import blurFace
from Source.Anonymise import detectFace

lena = '../hdr-bilder/Faces/lena.png'
group1 = '../hdr-bilder/Faces/group1.jpg'
couple = '../hdr-bilder/Faces/couple.jpg'

class test_Anon(unittest.TestCase):
    """
    Tests for the anonymise module
    """
    def test_faceDetect_Lena(self):
        """
        Test for face detection of image (lena) 
        """
        lena_antall, lena_image = detectFace(lena)
        lena_expectedNumber = 1
        self.assertEqual(lena_antall, lena_expectedNumber)
     
    
    def test_faceDetect_Group1(self):
        """
        Test for face detection of image (group1.jpg)
        """
        group1_antall, group1_image = detectFace(group1)
        group1_expectedNumber = 7
        self.assertEqual(group1_antall, group1_expectedNumber)
        
    def test_faceDetect_Couple(self):
        """
        Test for face detection of image (couple.jpg)
        """
        couple_antall, couple_image = detectFace(couple)
        couple_expectedNumber = 2
        self.assertEqual(couple_antall, couple_expectedNumber)