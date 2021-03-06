
import numpy as np
import argparse
from matplotlib import pyplot as plt
import time
import cv2

#aux func
def sliding_window(image, stepSize, windowSize):
	# slide window
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

#aux func to plot one row
def images_plotter(img, r, y_index):
    gaussian_img = cv2.GaussianBlur(img,(5,5), r)
    equalized_img = cv2.equalizeHist(gaussian_img)

    title = "r={}".format(r)

    plt.subplot(5,3,y_index),plt.imshow(gaussian_img, cmap = 'gray')
    plt.title(title), plt.xticks([]), plt.yticks([])

    plt.subplot(5,3,y_index+1),plt.imshow(cv2.equalizeHist(gaussian_img), cmap = 'gray')
    plt.title('Equalized'), plt.xticks([]), plt.yticks([])

    plt.subplot(5,3,y_index+2),plt.hist(cv2.equalizeHist(gaussian_img).ravel(),256,[0,256]) 
    plt.title('Equalized Histogram'), plt.xticks([]), plt.yticks([])

#aux func to all rows with r values
def image_plotter_incrementation(img):
    r_values = [0.001, 0.75, 1, 5]
    y_index = 4

    for r_value in r_values:
        images_plotter(img,r_value,y_index)
        y_index = y_index+3


# load the image and define window size/proportions
img_color = cv2.imread("./images/imageNoise.jpg")
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
result = img.copy()
(window_width, window_height) = (10, 10)

	
plt.subplot(531),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(532),plt.imshow(cv2.equalizeHist(img), cmap = 'gray')
plt.title('Equalized'), plt.xticks([]), plt.yticks([])

plt.subplot(533),plt.hist(cv2.equalizeHist(img).ravel(),256,[0,256]) 
plt.title('Equalized Histogram'), plt.xticks([]), plt.yticks([])

image_plotter_incrementation(img)

#Show everything
plt.show()
