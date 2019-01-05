from FiltrationLimitsBase import *

class HSVLimits (FiltrationLimitsBase):
    def __init__(self):
        self.minH = 0
        self.minS = 0
        self.minV = 0
        
        self.maxH = 0
        self.maxS = 0
        self.maxV = 0