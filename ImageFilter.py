from FiltrationBase import *

class ImageFilter (FiltrationBase):
    def __init__(self, image, target):
        super().__init__(target)
        self.image = image