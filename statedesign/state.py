"""  The Camera class is the context. A camera behaves differently
    when the camera is in different modes(states). """
class Camera :
    def __init__(self, mode, zoomLevel, usingFrontCamera) :
        """  Set current mode(state)  """
        self._currentMode = mode
        self._zoomLevel = zoomLevel
        self._usingFrontCamera = usingFrontCamera
    
    
    """  Change current mode(state)   """
    def changeMode(self, mode) : self._currentMode = mode 
    
    """  Uses the mode's (state's) version of the main .
        Refers to the specific state function.   """
    def mainButton(self) : return self._currentMode.mainButton() 


"""  CameraModes class is an interface(virtual) class for the
    the mode(state) classes below. """
class CameraModes :
    def __init__( mode) :
        currentMode = mode
    
    def mainButton(self, action) :
        return action
        

"""  Portrait Mode and Video Mode classes extend upon the CameraModes class.
    Below classes are the state classes. """
class PortraitMode(CameraModes):
    def __init__(self) -> CameraModes.__init__('Portrait Mode'):
        pass
    def mainButton(self) :
        return CameraModes.mainButton(self, "Portrait Taken")
    


class VideoMode(CameraModes):
    def __init__(self) -> CameraModes.__init__('Video Mode'):
        pass
    
    def mainButton(self) :
        return CameraModes.mainButton(self,"Video Filmed") 