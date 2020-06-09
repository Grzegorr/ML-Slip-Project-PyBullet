#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import graphics


class Interface:
# Define a main function and instantiate the window object.
    def __init__(self):
        print()
        self.win = graphics.GraphWin("Exercise-01", 1600, 500)
    
    
    def updateWindow(self,proximal1, proximal2, proximal3, distal1, distal2, distal3):
        self.clear()
        
        #print("AAA")
        proximal1_0 = "{:.4f}".format(proximal1[0])
        proximal1_1 = "{:.4f}".format(proximal1[1])
        proximal1_2 = "{:.4f}".format(proximal1[2])
        proximal1_3 = "{:.4f}".format(proximal1[3])
        proximal1_4 = "{:.4f}".format(proximal1[4])
        
        proximal2_0 = "{:.4f}".format(proximal2[0])
        proximal2_1 = "{:.4f}".format(proximal2[1])
        proximal2_2 = "{:.4f}".format(proximal2[2])
        proximal2_3 = "{:.4f}".format(proximal2[3])
        proximal2_4 = "{:.4f}".format(proximal2[4])
        
        proximal3_0 = "{:.4f}".format(proximal3[0])
        proximal3_1 = "{:.4f}".format(proximal3[1])
        proximal3_2 = "{:.4f}".format(proximal3[2])
        proximal3_3 = "{:.4f}".format(proximal3[3])
        proximal3_4 = "{:.4f}".format(proximal3[4])
        
        distal1_0 = "{:.4f}".format(distal1[0])
        distal1_1 = "{:.4f}".format(distal1[1])
        distal1_2 = "{:.4f}".format(distal1[2])
        distal1_3 = "{:.4f}".format(distal1[3])
        
        distal2_0 = "{:.4f}".format(distal2[0])
        distal2_1 = "{:.4f}".format(distal2[1])
        distal2_2 = "{:.4f}".format(distal2[2])
        distal2_3 = "{:.4f}".format(distal2[3])
        
        distal3_0 = "{:.4f}".format(distal3[0])
        distal3_1 = "{:.4f}".format(distal3[1])
        distal3_2 = "{:.4f}".format(distal3[2])
        distal3_3 = "{:.4f}".format(distal3[3])
        
        #Draw the palm
        palm = graphics.Rectangle(graphics.Point(650, 125), graphics.Point(950, 375))
        palm.draw(self.win)
    
        #Draw finger 1
        proximal1 = graphics.Rectangle(graphics.Point(975, 300), graphics.Point(1300, 350))
        proximal1.draw(self.win)
        self.fillProximal1(proximal1_0,proximal1_1,proximal1_2,proximal1_3,proximal1_4,self.win)
        distal1 = graphics.Rectangle(graphics.Point(1325, 300), graphics.Point(1590, 350))
        distal1.draw(self.win)
        self.fillDistall1(distal1_0,distal1_1,distal1_2,distal1_3,self.win)
        
        #Draw finger 2
        proximal2 = graphics.Rectangle(graphics.Point(975, 150), graphics.Point(1300, 200))
        proximal2.draw(self.win)
        self.fillProximal2(proximal2_0,proximal2_1,proximal2_2,proximal2_3,proximal2_4,self.win)
        distal2 = graphics.Rectangle(graphics.Point(1325, 150), graphics.Point(1590, 200))
        distal2.draw(self.win)
        self.fillDistall2(distal2_0,distal2_1,distal2_2,distal2_3,self.win)
        
        #Draw finger 3
        proximal3 = graphics.Rectangle(graphics.Point(300, 225), graphics.Point(625, 275))
        proximal3.draw(self.win)
        self.fillProximal3(proximal3_0,proximal3_1,proximal3_2,proximal3_3,proximal3_4,self.win)
        distal3 = graphics.Rectangle(graphics.Point(10, 225), graphics.Point(275, 275))
        distal3.draw(self.win)
        self.fillDistall3(distal3_0,distal3_1,distal3_2,distal3_3,self.win)
        
        
        #win.getMouse()
    
    def printText(self,x,y,colour,msg,size,style, font,win):  
        p = graphics.Point(x, y)
        t = graphics.Text(p, msg)
        t.setTextColor(graphics.color_rgb(colour[0],colour[2],colour[2]))
        t.setSize(size)
        t.setStyle(style)
        t.setFace(font)
        t.draw(win)

        
    def fillProximal1(self,sens1msg,sens2msg,sens3msg,sens4msg,sens5msg,win):
        self.printText(1000, 325, [255,255,255], sens1msg, 12, "bold", "arial",win)
        self.printText(1070, 325, [255,255,255], sens2msg, 12, "bold", "arial",win)
        self.printText(1140, 325, [255,255,255], sens3msg, 12, "bold", "arial",win)
        self.printText(1210, 325, [255,255,255], sens4msg, 12, "bold", "arial",win)
        self.printText(1270, 325, [255,255,255], sens5msg, 12, "bold", "arial",win)
        
    def fillDistall1(self,sens1msg,sens2msg,sens3msg,sens4msg,win):
        self.printText(1350, 325, [255,255,255], sens1msg, 12, "bold", "arial",win)
        self.printText(1420, 325, [255,255,255], sens2msg, 12, "bold", "arial",win)
        self.printText(1490, 325, [255,255,255], sens3msg, 12, "bold", "arial",win)
        self.printText(1560, 325, [255,255,255], sens4msg, 12, "bold", "arial",win)

    def fillProximal2(self,sens1msg,sens2msg,sens3msg,sens4msg,sens5msg,win):
        self.printText(1000, 175, [255,255,255], sens1msg, 12, "bold", "arial",win)
        self.printText(1070, 175, [255,255,255], sens2msg, 12, "bold", "arial",win)
        self.printText(1140, 175, [255,255,255], sens3msg, 12, "bold", "arial",win)
        self.printText(1210, 175, [255,255,255], sens4msg, 12, "bold", "arial",win)
        self.printText(1270, 175, [255,255,255], sens5msg, 12, "bold", "arial",win)
    
    def fillDistall2(self,sens1msg,sens2msg,sens3msg,sens4msg,win):
        self.printText(1350, 175, [255,255,255], sens1msg, 12, "bold", "arial",win)
        self.printText(1420, 175, [255,255,255], sens2msg, 12, "bold", "arial",win)
        self.printText(1490, 175, [255,255,255], sens3msg, 12, "bold", "arial",win)
        self.printText(1560, 175, [255,255,255], sens4msg, 12, "bold", "arial",win)
    
    def fillProximal3(self,sens1msg,sens2msg,sens3msg,sens4msg,sens5msg,win):
        self.printText(600, 250, [255,255,255], sens1msg, 12, "bold", "arial",win)
        self.printText(530, 250, [255,255,255], sens2msg, 12, "bold", "arial",win)
        self.printText(460, 250, [255,255,255], sens3msg, 12, "bold", "arial",win)
        self.printText(390, 250, [255,255,255], sens4msg, 12, "bold", "arial",win)
        self.printText(320, 250, [255,255,255], sens5msg, 12, "bold", "arial",win)
    
    def fillDistall3(self,sens1msg,sens2msg,sens3msg,sens4msg,win):
        self.printText(250, 250, [255,255,255], sens1msg, 12, "bold", "arial",win)
        self.printText(180, 250, [255,255,255], sens2msg, 12, "bold", "arial",win)
        self.printText(110, 250, [255,255,255], sens3msg, 12, "bold", "arial",win)
        self.printText(50, 250, [255,255,255], sens4msg, 12, "bold", "arial",win)

    def clear(self):
        for item in self.win.items[:]:
            item.undraw()
        self.win.items = []




