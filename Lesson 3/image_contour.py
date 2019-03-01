# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:53:07 2019

@author: useraccountname
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('images/thumbs_up_down.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.imshow(gray,cmap='gray')

retval,binary=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)
plt.imshow(binary,cmap='gray')

retval,contour,hierachy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contour_image=np.copy(img)
contour_image=cv2.drawContours(contour_image,contour,-1,(255,0,0),3)

plt.imshow(contour_image)


