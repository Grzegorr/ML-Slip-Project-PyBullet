#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:38:14 2020

@author: grzegorz
"""
import pybullet as p
import numpy as np


task = [ [ 6500, [0.5,0,0.6], p.getQuaternionFromEuler([1.57,0,0]), 0, 1, 1, 1 ],
          [ 7000, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ],
          [ 7500, [0.5,0.5,0.6], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
          [ 8000, [0.3,0.3,0.3], p.getQuaternionFromEuler([-1.57,0,0]), 1, 1, 1, 1 ],
          [ 8500, [0.5,0.5,0.6], p.getQuaternionFromEuler([1.57,0,0]), 1, 1, 1, 1 ]
        ]
entryName = "ArmHitTable.npy"
fileName = "Tasks/" + entryName
np.save(fileName, task)