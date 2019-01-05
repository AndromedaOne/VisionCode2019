from HSVLimits import *
from NumberOfContoursLimit import *
from LengthToWidthRatioLimits import *
from SizeLimits import *
from PercentWhitePixelsLimits import *

class TargetData:
    def __init__(self):
        self.hSV = HSVLimits()
        self.numberOfContours = NumberOfContoursLimit()
        self.lengthToWidthRatio = LengthToWidthRatioLimits()
        self.size = SizeLimits()
        self.percentWhitePixels = PercentWhitePixelsLimits()

