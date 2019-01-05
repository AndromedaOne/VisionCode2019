#import ImageCaptureBase
from ImageCaptureBase import *

class RaspberryPiCamera (ImageCaptureBase):
    def __init__(self):
        super().__init__()

    def getImage(self, imageData):
        imageData.unfilteredImage = 0
        return
        #This does not work yet...