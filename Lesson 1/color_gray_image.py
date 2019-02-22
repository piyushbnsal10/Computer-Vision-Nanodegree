# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:18:51 2019

@author: useraccountname
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

image =cv2.imread('images/waymo_car.jpg')

print(image.shape)

gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
print(gray_image.shape)
plt.imshow(image,cmap='gray')