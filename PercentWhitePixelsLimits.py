from FiltrationLimitsBase import *

class PercentWhitePixelsLimits (FiltrationLimitsBase):
    def __init__(self):
        self.percentWhitePixelsMin = 0.0
        self.percentWhitePixelsMax = 0.0