#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import *

#calOutputName = "Calibration2"
calOutputName = "Calibration_cylinder"
#calOutputName = "Calibration_cylinder2"
#calOutputName = "Calibration_cylinder3"

def PolarToCartesian(vec):
    r = vec[0]
    angle = vec[1]
    angle = angle/18.0*3.14
    x = r * cos(angle)
    y = r * sin(angle)
    return [x,y]

def facingFlat():
    calibrationResult = np.load("Calibration/" + calOutputName + ".npy", allow_pickle = True)
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
    fig = plt.figure()    
    plt.polar(horizontalCirclePlot[:,0],horizontalCirclePlot[:,1])
    plt.title("Facing Flat")
    plt.show()
    fig.savefig('FacingFlatAccl_' + calOutputName + '.png')
        
    #plt.plot(horizontalCirclePlot[:,0],horizontalCirclePlot[:,1])
    #plt.ylim([-1000,1000])
    #plt.xlim([-1000,1000])
    #plt.show()

def horizontal():
    calibrationResult = np.load("Calibration/" + calOutputName + ".npy", allow_pickle = True)
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
    fig = plt.figure()
    plt.polar(CirclePlot[:,0],CirclePlot[:,1])
    plt.title("Horizontal Circle")
    plt.show()
    fig.savefig('HorizontalAccl_' + calOutputName + '.png')
   
    
def facingEdge():
    calibrationResult = np.load("Calibration/" + calOutputName + ".npy", allow_pickle = True)
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
    fig = plt.figure()
    plt.polar(CirclePlot[:,0],CirclePlot[:,1])
    plt.title("Facing Edge Circle")
    plt.show()
    fig.savefig('FacingEdgeAccl_' + calOutputName + '.png')
    
horizontal()
facingFlat()
facingEdge()




