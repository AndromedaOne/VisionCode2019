import cv2
from ImageFilter import * 

class Contours (ImageFilter):

    def __init__(self, image, target):
        super().__init__(self, image, target)
        self.numberOfContours = 0
    
    def run(self):
        throwawayImage, contours, hierarchy = cv2.findContours(self.image, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        self.boundingBoxes = []
        for box in contours:
            if len(box)>= self.numberOfContours:
                self.boundingBoxes = self.boundingBoxes + [cv2.boundingRect(box)]
        #Returns BOUNDING BOXES!!!!
        return 

    def getFilteredArray(self):
        return self.boundingBoxes
    