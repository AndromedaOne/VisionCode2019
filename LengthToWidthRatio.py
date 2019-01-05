from FiltrationBase import *
import cv2

class LengthToWidthRatio (FiltrationBase):
    def __init__(self, lengthToWidthRatioLimits, boundingBoxesOfTargetCandidates):
        self.lengthToWidthRatioLimits = lengthToWidthRatioLimits
        self.boundingBoxesOfTargetCandidates = boundingBoxesOfTargetCandidates

    def run(self):
        #Filters out all "Blobs" with length to width ratios not between lowLengthToWidthRatio and highLengthToWidthRatio        
        betterBoundingBoxes = []
        for box in self.boundingBoxesOfTargetCandidates:
            width = box[2]
            height = box[3]
            lengthToWidthRatioOfBoundingBox = (width + 0.0)/(height+ 0.0)
            
            if self.lengthToWidthRatioLimits.lowLengthToWidthRatio < lengthToWidthRatioOfBoundingBox < self.lengthToWidthRatioLimits.highLengthToWidthRatio:
                betterBoundingBoxes = betterBoundingBoxes + [box]
        
        return betterBoundingBoxes
