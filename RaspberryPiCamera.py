#import ImageCaptureBase
from ImageCaptureBase import *

class RaspberryPiCamera (ImageCaptureBase):
    def __init__(self):
        super().__init__()

    def getImage(self):
        return 0
        #This does not work yet...