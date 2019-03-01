# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:04:47 2019

@author: useraccountname
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


image=cv2.imread('images/waffle.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
copy_image=np.copy(image)
plt.imshow(image)

gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,3,0.04)
dst=cv2.dilate(dst,None)
#print(image.shape)
#print(dst.shape)

plt.imshow(dst,cmap='gray')

threshold=0.1*dst.max()

for i in range(dst.shape[0]):
    for j in range(dst.shape[1]):
        if(dst[i,j]>threshold):
            cv2.circle(copy_image,(j,i),1,(0,0,255),1)

plt.imshow(copy_image)