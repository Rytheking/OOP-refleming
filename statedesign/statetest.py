import unittest

from state import *


class CameraTest(unittest.TestCase):
    def testDefaultCamera(self):
        portraitMode = PortraitMode()
        videoMode = VideoMode()
        phone: Camera = Camera(portraitMode, 1, False)
        self.assertEqual(phone.mainButton(), "Portrait Taken")
        
        phone.changeMode(videoMode)
        self.assertEqual(phone.mainButton(), "Video Filmed")

        phone.changeMode(portraitMode)
        self.assertEqual(phone.mainButton(), "Portrait Taken")

if __name__ == '__main__':
    unittest.main()
