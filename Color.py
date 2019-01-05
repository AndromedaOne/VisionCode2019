import cv2
from FiltrationBase import *

class Color (FiltrationBase):
    def __init__(self, hSVLimits, image):
        self.hSVLimits = hSVLimits
        self.image = image
    
    def run(self):
        filteredHSVImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        filteredHSVImage = cv2.inRange(filteredHSVImage,(self.hSVLimits.minH,self.hSVLimits.minS,self.hSVLimits.minV),(self.hSVLimits.maxH,self.hSVLimits.maxS,self.hSVLimits.maxV))
        
        return filteredHSVImage
