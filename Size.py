from BoundingBoxFilter import *
import cv2

class Size (BoundingBoxFilter):
    def __init__(self, boundingBoxes, target):
        super().__init__(self, boundingBoxes, target)
        self.minHeightSize = 0
        self.maxHeightSize = 0
        self.minWidthSize = 0
        self.maxWidthSize = 0

    def run(self):
       #Filters out "Blobs" that are way too big or way too small
        for box in self.boundingBoxes:
            width = box[2]
            height = box[3]
            if self.minHeightSize < height < self.maxHeightSize and self.minWidthSize < width < self.maxWidthSize:
                self.betterBoundingBoxes = self.betterBoundingBoxes + [box]
        return
