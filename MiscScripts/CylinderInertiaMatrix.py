#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def inertialTensorOfCylinder(M,h,r):
    ixx = 1.0/12.0*M*h*h + 1.0/4.0*M*r*r
    iyy = ixx
    izz = 0.5*M*r*r
    ixy = 0
    ixz = 0
    iyx = 0
    print("ixx=\""+ str(ixx) + "\" ixy=\"0\" ixz=\"0\" iyy=\"" + str(iyy) + "\" iyz=\"0\" izz=\"" + str(izz) + "\"")
    

print("Cylinder")
inertialTensorOfCylinder(0.5, 0.2, 0.02)    
print("Cylinder2")
inertialTensorOfCylinder(0.2, 0.2, 0.02)   
print("Cylinder3")
inertialTensorOfCylinder(1.0, 0.2, 0.02)   
    
