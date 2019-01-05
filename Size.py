from FiltrationBase import *
import cv2

class Size (FiltrationBase):
    def __init__(self, sizeLimits, boundingBoxesOfTargetCandidates):
        
        self.sizeLimits = sizeLimits
        self.boundingBoxesOfTargetCandidates = boundingBoxesOfTargetCandidates

    def run(self):
        #Filters out "Blobs" that are way too big or way too small
        self.betterBoundingBoxes = []
        for box in self.boundingBoxesOfTargetCandidates:
            width = box[2]
            height = box[3]
            
            if self.sizeLimits.minHeightSize < height < self.sizeLimits.maxHeightSize and self.sizeLimits.minWidthSize < width < self.sizeLimits.maxWidthSize:
                self.betterBoundingBoxes = self.betterBoundingBoxes + [box]

        return self.betterBoundingBoxes
