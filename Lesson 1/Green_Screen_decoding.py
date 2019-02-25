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
img=cv2.imread('images/car_green_screen.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)


#getting the blue part
lower_bound=np.array([20,210,20])
upper_bound=np.array([150,255,150])

new_img=cv2.inRange(img,lower_bound,upper_bound)
plt.imshow(new_img,cmap='gray')
img[new_img !=0]=[0,0,0]
plt.imshow(img)


back_img=cv2.imread('images/sky.jpg')
back_img=cv2.cvtColor(back_img,cv2.COLOR_BGR2RGB)
back_img=back_img[:450,:660]
plt.imshow(back_img)

back_img[new_img ==0]=[0,0,0]
plt.imshow(back_img)

final_img=back_img + img
plt.imshow(final_img)