from FiltrationBase import *

class BoundingBoxFilter (FiltrationBase):
    
    def __init__(self, boundingBoxes, target):
        super().__init__(target)
        self.boundingBoxes = boundingBoxes
        self.betterBoundingBoxes = []
    
    def getFilteredArray(self):
        return self.betterBoundingBoxes