# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:29:02 2019

@author: useraccountname
"""

import cv2
import matplotlib.pyplot as plt

image=cv2.imread('images/wa_state_highway.jpg')

r=image[: , : ,0]
b=image[: , : ,1]
g=image[: , : ,2]

f,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(20,10))
ax1.imshow(r,cmap='gray')
ax2.imshow(b,cmap='gray')
ax3.imshow(g,cmap='gray')