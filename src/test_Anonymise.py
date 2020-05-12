import unittest
from Source.Anonymise import blurFace
from Source.Anonymise import detectFace

lena = '../hdr-bilder/Faces/lena.png'
team = '../hdr-bilder/Faces/team.jpg'

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
     
    
    def test_faceDetect_Team(self):
        """
        Test for face detection of image (team)
        """
        team_antall, team_image = detectFace(team, 1.25037, 3)
        team_expectedNumber = 8
        self.assertEqual(team_antall, team_expectedNumber)