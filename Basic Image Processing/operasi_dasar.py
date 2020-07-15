# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:40:18 2020

@author: Fidelis Galla 
"""

#mengakses library
import cv2
import config

img = cv2.imread(config.img_path)

#mengakses pixel pada koordinat tertentu
px = img[100,100]

print(px)

#mengakses pixel untuk nilai blue
px_blue = px[2]
print(px_blue)

#mengakses shape dari image
shape = img.shape
print(shape)

#mengakses total pixel 
size = img.size
print(size)

ROI = img[40:100,80:280]
cv2.imshow('frame',ROI)
cv2.waitKey(0)
cv2.destroyAllWindows()
