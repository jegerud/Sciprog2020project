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
        lena_antall, lena_image = detectFace(lena)
        team_antall, team_image = detectFace(team)
        
        lena_expectedNumber = 1
        team_expectedNumber = 8
        
        self.assertEqual(lena_antall, lena_expectedNumber)
        self.assertEqual(team_antall, team_expectedNumber)
    
    
    