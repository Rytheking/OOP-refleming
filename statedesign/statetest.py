import unittest

from state import Camera, CameraModes


class CameraTest(unittest.TestCase):
    def testDefaultCamera(self):
        portraitMode = PortraitMode()
        videoMode = VideoMode()
        phone: Camera = Camera(portraitMode, 1, false)
        self.assertEqual(phone.mainButton(), "Portrait Taken")
        
        Phone.changeMode(videoMode)
        self.assertEqual(phone.mainButton(), "Video Filmed")

        Phone.changeMode(portraitMode)
        self.assertEqual(phone.mainButton(), "Portrait Taken")
