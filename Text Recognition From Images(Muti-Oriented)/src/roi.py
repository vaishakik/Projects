#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:49:05 2018

@author: shocked
"""

from imutils import paths
import imutils 
import numpy as np
import argparse
import imutils
import cv2
 
# initialize a rectangular and square structuring kernel
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))
image = cv2.imread('/home/shocked/Desktop/D/FCN_Text-master/i/1.jpg')
image1 = cv2.imread('/home/shocked/Downloads/MSRA-TD500/test/IMG_1972.JPG')
image = imutils.resize(image, height=600)
image1 = imutils.resize(image1, height=600)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (3, 3), 0)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8") 
    
p = int(image.shape[1] * 0.05)
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
thresh = cv2.erode(thresh, None, iterations=4)

thresh[:, 0:p] = 0
thresh[:, image.shape[1] - p:] = 0
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
#print(cnts)
 
	# loop over the contours
for c in cnts:
   (x, y, w, h) = cv2.boundingRect(c)
   ar = w / float(h)
   rect = cv2.minAreaRect(c)
   box = cv2.boxPoints(rect)
   print(rect)
   print("\n\n")
   print(rect[2]*((22/7)/180))
   box = np.int0(box)
   cv2.drawContours(image1,[box],0,(0,0,255),2)
   crWidth = w / float(gray.shape[1])
   if ar > 5 and crWidth > 0.75:
        pX = int((x + w) * 0.03)
        pY = int((y + h) * 0.03)
        (x, y) = (x - pX, y - pY)
        (w, h) = (w + (pX * 2), h + (pY * 2))
        roi = image[y:y + h, x:x + w].copy()
        cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        break
 
	# show the output images
cv2.imshow("Image", image1)
#cv2.imshow("Image", thresh)
#cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()



    
