from BoundingBoxFilter import *
import cv2

class LengthToWidthRatio (BoundingBoxFilter):
    def __init__(self, boundingBoxes, target):
        super().__init__(self,boundingBoxes, target)
        self.lowLengthToWidthRatio = 0
        self.highLengthToWidthRatio = 0

    def run(self):
        #Filters out all "Blobs" with length to width ratios not between lowLengthToWidthRatio and highLengthToWidthRatio        
        for box in self.boundingBoxes:
            width =  box[2]
            height =  box[3]

            #print 'lowLengthToWidthRatio < (width + 0.0)/ (height+ 0.0) < highLengthToWidthRatio', (width + 0.0)/ (height+ 0.0)
            if self.lowLengthToWidthRatio < (width + 0.0)/ (height+ 0.0) < self.highLengthToWidthRatio:
                self.betterBoundingBoxes = self.betterBoundingBoxes + [box]
        return
