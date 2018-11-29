import cv2
from ImageFilter import *

class Color (ImageFilter):
    def __init__(self, image, target):
        super().__init__(self, image, target)
        self.minH = 0
        self.minS = 0
        self.minV = 0
        
        self.maxH = 0
        self.maxS = 0
        self.maxV = 0
    
    def run(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.image = cv2.inRange(self.image,(self.minH,self.minS,self.minV),(self.maxH,self.maxS,self.maxV))
        return

    def getFilteredImage(self):
        return self.image

