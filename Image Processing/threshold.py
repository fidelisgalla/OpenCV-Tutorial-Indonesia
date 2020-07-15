# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:55:07 2020

@author: fidelis.limbong
"""
import cv2
#load the image
img = cv2.imread('food.jpg')
resize = cv2.resize(img,(300,300))
gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200)
cv2.imshow('detector',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()