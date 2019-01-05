import cv2
from FiltrationBase import *

class Contours (FiltrationBase):

    def __init__(self, numberOfContoursLimit, image):
        self.numberOfContoursLimit = numberOfContoursLimit
        self.image = image
    
    def run(self):
        throwawayImage, contours, hierarchy = cv2.findContours(self.image, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        boundingBoxes = []
        for box in contours:
            if len(box)>= self.numberOfContoursLimit.numberOfContours:
                boundingBoxes = boundingBoxes + [cv2.boundingRect(box)]

        #Returns BOUNDING BOXES!!!!
        return boundingBoxes
    