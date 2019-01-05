import cv2

class ImageDebugger:

    def __init__(self, image, boundingBoxesOfTargetCandidates, name):
        self.image = image
        self.boundingBoxesOfTargetCandidates = boundingBoxesOfTargetCandidates
        self.name = name
    
    def displayImage(self):
        cv2.imshow(self.name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def displayImageWithBoundingBoxes(self):
        copy = self.image.copy()
        if(len(copy.shape) == 2): # if the image has two channels
            copy = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)
        
        for box in self.boundingBoxesOfTargetCandidates:
            x,y,width,height = box
            copy = cv2.rectangle(copy,(x,y),((x + width), (y + height)),(0,0,255), 3)
        
        cv2.imshow(self.name, copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()