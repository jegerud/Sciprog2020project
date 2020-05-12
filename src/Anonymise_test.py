import unittest
from Source.Anonymise import blurFace
from Source.Anonymise import detectFace

lena = '../../hdr-bilder/Faces/lena.png'
team = '../../hdr-bilder/Faces/team.jpg'

class test_Anon(unittest.TestCase):
    """
    Tests for the anonymise module
    """
    def test_faceDetect(self):
        """
        test for face detection
        """
        lena_antall, lena_image = detectFace(lena)
        team_antall, team_image = detectFace(team, 1.25037, 3)
        
        lena_expectedNumber = 1
        team_expectedNumber = 8
        
        self.assertEqual(lena_antall, lena_expectedNumber)
        self.assertEqual(team_antall, team_expectedNumber)
    
    
if __name__ == '__main__':
    unittest.main()  