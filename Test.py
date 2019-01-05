import cv2
import numpy as np
import os

from ImageDebugger import *
from TargetData import *

from Color import *
from Contours import *
from Size import *
from LengthToWidthRatio import *
from PercentWhitePixels import *

def myMain():
    pics = '/Users/seandoyle/git/AndromedaVision/WPIPics'
    myTarget = createSampleTarget() 

    for filename in os.listdir(pics):
        fullFileName = os.path.join(pics, filename)
        image = cv2.imread(fullFileName)
        
        boundingBoxesOfTargetCandidates = []
        normalImageDebugger = ImageDebugger(image, boundingBoxesOfTargetCandidates, "Normal Image")
        normalImageDebugger.displayImage()
        
        colorFilter = Color(myTarget.hSV, image)
        hSVFilteredImage = colorFilter.run()
        hSVFilteredImageDebugger = ImageDebugger(hSVFilteredImage, boundingBoxesOfTargetCandidates, "HSV")
        hSVFilteredImageDebugger.displayImage()

        contourFilter = Contours(myTarget.numberOfContours, hSVFilteredImage)
        boundingBoxesOfTargetCandidates = contourFilter.run()
        contourFilterDebugger = ImageDebugger(image, boundingBoxesOfTargetCandidates, "Contour")
        contourFilterDebugger.displayImageWithBoundingBoxes()

        sizeFilter = Size(myTarget.size, boundingBoxesOfTargetCandidates)
        boundingBoxesOfTargetCandidates = sizeFilter.run()
        sizeFilterDebugger = ImageDebugger(image, boundingBoxesOfTargetCandidates, "Size")
        sizeFilterDebugger.displayImageWithBoundingBoxes()

        lengthToWidthRatioFilter = LengthToWidthRatio(myTarget.lengthToWidthRatio, boundingBoxesOfTargetCandidates)
        boundingBoxesOfTargetCandidates = lengthToWidthRatioFilter.run()
        lengthToWidthRatioDebugger = ImageDebugger(image, boundingBoxesOfTargetCandidates, "LengthToWidth")
        lengthToWidthRatioDebugger.displayImageWithBoundingBoxes()

        percentWhitePixelsFilter = PercentWhitePixels(myTarget.percentWhitePixels, boundingBoxesOfTargetCandidates, hSVFilteredImage)
        boundingBoxesOfTargetCandidates = percentWhitePixelsFilter.run()
        percentWhitePixelsDebugger = ImageDebugger(hSVFilteredImage, boundingBoxesOfTargetCandidates, "percentWhitePixels")
        percentWhitePixelsDebugger.displayImageWithBoundingBoxes()


def createSampleTarget():
    target = TargetData()
    target.hSV.minH = 55
    target.hSV.minS = 10
    target.hSV.minV = 5
    target.hSV.maxH = 65
    target.hSV.maxS = 255
    target.hSV.maxV = 255

    target.numberOfContours.numberOfContours = 2   

    target.size.maxHeightSize = 2500
    target.size.maxWidthSize = 1500
    target.size.minHeightSize = 35
    target.size.minWidthSize = 15

    target.lengthToWidthRatio.highLengthToWidthRatio = 0.6
    target.lengthToWidthRatio.lowLengthToWidthRatio = 0.4

    target.percentWhitePixels.percentWhitePixelsMax = 1.000
    target.percentWhitePixels.percentWhitePixelsMin = 0.700
    return target

myMain()