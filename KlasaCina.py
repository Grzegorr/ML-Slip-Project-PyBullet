#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

class KC:
    
    def __init__(self):
        self.czas = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        
    def dlugosc(self):
        self.czas2= time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        print(self.czas2-self.czas)
        self.czas = self.czas2
