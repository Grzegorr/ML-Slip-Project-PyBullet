#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import *

def PolarToCartesian(vec):
    r = vec[0]
    angle = vec[1]
    angle = angle/18.0*3.14
    x = r * cos(angle)
    y = r * sin(angle)
    return [x,y]

def horizontal():
    calibrationResult = np.load("Calibration/Calibration1.npy", allow_pickle = True)
    #print(calibrationResult)
    #print()
    #print(calibrationResult[:,9])
    
    #Hand is heading upwards wit fingers
    #resiliance on the horizontal circle
    horizontalCircle = calibrationResult[:,9]
    horizontalCirclePlot = np.zeros((37,2))
    for x in range(36):
        horizontalCirclePlot[x] = [x/18.0*3.14,horizontalCircle[x]]
    horizontalCirclePlot[36] = horizontalCirclePlot[0]
        
    plt.polar(horizontalCirclePlot[:,0],horizontalCirclePlot[:,1])
    plt.title("Horizontal Circle")
    plt.show()
    plt.savefig('horizontalCircleAccelerations.png')
        
    #plt.plot(horizontalCirclePlot[:,0],horizontalCirclePlot[:,1])
    #plt.ylim([-1000,1000])
    #plt.xlim([-1000,1000])
    #plt.show()

def facingFlat():
    calibrationResult = np.load("Calibration/Calibration1.npy", allow_pickle = True)
    HalfCircle1 = calibrationResult[9,:]
    HalfCircle2 = calibrationResult[27,:]
    HalfCircle2 = HalfCircle2[::-1]
    fullCircle = [*HalfCircle1,*HalfCircle2,*[0]]
    print(fullCircle)
    fullCircle[36] = fullCircle[0]
    print()
    print(fullCircle)
    #print(fullCircle)
    
    CirclePlot = np.zeros((37,2))
    for x in range(37):
        CirclePlot[x] = [x/18.0*3.14,fullCircle[x]]
    plt.polar(CirclePlot[:,0],CirclePlot[:,1])
    plt.title("Facing Flat Circle")
    plt.show()
    plt.savefig('FacingFlatCircleAccelerations.png')
   
    
def facingEdge():
    calibrationResult = np.load("Calibration/Calibration1.npy", allow_pickle = True)
    HalfCircle1 = calibrationResult[0,:]
    HalfCircle2 = calibrationResult[18,:]
    HalfCircle2 = HalfCircle2[::-1]
    fullCircle = [*HalfCircle1,*HalfCircle2,*[0]]
    print(fullCircle)
    fullCircle[36] = fullCircle[0]
    print()
    print(fullCircle)
    #print(fullCircle)
    
    CirclePlot = np.zeros((37,2))
    for x in range(37):
        CirclePlot[x] = [x/18.0*3.14,fullCircle[x]]
    plt.polar(CirclePlot[:,0],CirclePlot[:,1])
    plt.title("Facing Edge Circle")
    plt.show()
    plt.savefig('FacingEdgeCircleAccelerations.png')
    
horizontal()
facingFlat()
facingEdge()




