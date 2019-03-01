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

retval,contours,hierachy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contour_image=np.copy(img)
contour_image=cv2.drawContours(contour_image,contours,-1,(255,0,0),3)

plt.imshow(contour_image)


## TODO: Complete this function so that 
## it returns the orientations of a list of contours
## The list should be in the same order as the contours
## i.e. the first angle should be the orientation of the first contour
def orientations(contours):
    """
    Orientation 
    :param contours: a list of contours
    :return: angles, the orientations of the contours
    """
    
    # Create an empty list to store the angles in
    # Tip: Use angles.append(value) to add values to this list
    angles = []
    for i in range(len(contours)):
        (x,y),(MA,ma),angle=cv2.fitEllipse(contours[i])
        angles.append(angle)
    
    return angles


# ---------------------------------------------------------- #
# Print out the orientation values
angles = orientations(contours)
print('Angles of each contour (in degrees): ' + str(angles))


## TODO: Complete this function so that
## it returns a new, cropped version of the original image
def left_hand_crop(image, selected_contour):
    """
    Left hand crop 
    :param image: the original image
    :param selectec_contour: the contour that will be used for cropping
    :return: cropped_image, the cropped image around the left hand
    """
    
    ## TODO: Detect the bounding rectangle of the left hand contour
    x,y,w,h =cv2.boundingRect(selected_contour)
    box_image = cv2.rectangle(contour_image, (x,y), (x+w,y+h), (200,0,200),2)
    ## TODO: Crop the image using the dimensions of the bounding rectangle
    
    # Make a copy of the image to crop
    cropped_image = np.copy(image)
    cropped_image = cropped_image[y: y + h, x: x + w]
    
    
    return cropped_image


## TODO: Select the left hand contour from the list
## Replace this value
selected_contour = contours[1]


# ---------------------------------------------------------- #
# If you've selected a contour
if(selected_contour is not None):
    # Call the crop function with that contour passed in as a parameter
    cropped_image = left_hand_crop(img, selected_contour)
    plt.imshow(cropped_image)
