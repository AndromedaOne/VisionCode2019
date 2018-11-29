from BoundingBoxFilter import *
from ImageFilter import *
import cv2

class BlackToWhiteRatio (BoundingBoxFilter, ImageFilter):
    def __init__(self, boundingBoxes, image, target):
        super().__init__(self, boundingBoxes, target)
        super().__init__(self, image, target)
        self.blackToWhiteRatioMin = 0
        self.blackToWhiteRatioMax = 0
        

    def run(self):
        #Filters out all "Blobs" that do not have a ratio of white to black pixels between blackToWhiteRatioMin - blackToWhiteRatioMax 
        for box in self.boundingBoxes:
            x,y,width,height = box
            tempImage = self.image[y+height/2:y+height, x:x+width]     
            numberOfWhitePixels = cv2.countNonZero(tempImage)
            if self.blackToWhiteRatioMin < ((width*(height/2) - numberOfWhitePixels+ 0.0))/(numberOfWhitePixels) < self.blackToWhiteRatioMax:#number of black pixels for every white pixel
                self.betterBoundingBoxes = self.betterBoundingBoxes + [box]
        return
