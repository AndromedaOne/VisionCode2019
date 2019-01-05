from FiltrationBase import *
from ImageDebugger import *

import cv2

class PercentWhitePixels (FiltrationBase):
    def __init__(self, percentWhitePixelsLimits, boundingBoxesOfTargetCandidates, binaryImage):
        self.percentWhitePixelsLimits = percentWhitePixelsLimits
        self.boundingBoxesOfTargetCandidates = boundingBoxesOfTargetCandidates
        self.binaryImage = binaryImage

    def run(self):
        #Filters out all "Blobs" that do not have a ratio of white to black pixels between blackToWhiteRatioMin - blackToWhiteRatioMax 
        betterBoundingBoxes = []
        for box in self.boundingBoxesOfTargetCandidates:
            x,y,width,height = box
            tempImage = self.binaryImage[y:y+height, x:x+width]   
             
            numberOfWhitePixels = cv2.countNonZero(tempImage)
            percentWhitePixels = (numberOfWhitePixels)/((width + 0.0)*(height + 0.0))
            
            if self.percentWhitePixelsLimits.percentWhitePixelsMin < percentWhitePixels < self.percentWhitePixelsLimits.percentWhitePixelsMax:
                betterBoundingBoxes = betterBoundingBoxes + [box]
        
        return betterBoundingBoxes
