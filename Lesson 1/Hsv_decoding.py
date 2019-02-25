# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:57:34 2019

@author: useraccountname
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:26:04 2019

@author: useraccountname
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:14:30 2019

@author: useraccountname
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#CV2 reads image in bgr
img=cv2.imread('images/water_balloons.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)

copy_img=np.copy(img)

r=copy_img[:,:,0]
g=copy_img[:,:,1]
b=copy_img[:,:,2]

f,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(20,10))

ax1.set_title('RED')
ax1.imshow(r,cmap='gray')
ax2.set_title('GREEN')
ax2.imshow(g,cmap='gray')
ax3.set_title('BLUE')
ax3.imshow(b,cmap='gray')

#getting the blue part
lower_bound_rgb=np.array([180,20,100])
upper_bound_rgb=np.array([255,255,230])

new_img=cv2.inRange(copy_img,lower_bound_rgb,upper_bound_rgb)
plt.imshow(new_img,cmap='gray')
copy_img[new_img ==0]=[0,0,0]
plt.imshow(copy_img)

#HSV IMAGE
HSV_img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

h=HSV_img[:,:,0]
s=HSV_img[:,:,1]
v=HSV_img[:,:,2]

f,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(20,10))

ax1.set_title('HUE')
ax1.imshow(h,cmap='gray')
ax2.set_title('Saturation')
ax2.imshow(s,cmap='gray')
ax3.set_title('Value')
ax3.imshow(v,cmap='gray')

lower_bound_hsv=np.array([160,15,0])
upper_bound_hsv=np.array([300,255,255])

new_img=cv2.inRange(HSV_img,lower_bound_hsv,upper_bound_hsv)
HSV_img[new_img ==0]=[0,0,0]
plt.imshow(HSV_img)


