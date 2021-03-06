import numpy as np
import argparse
from matplotlib import pyplot as plt
import cv2

#aux func to avoid code repetition
def ploterFunction( imgs, titles, y_index):
    for index, img in enumerate(imgs):
        plt.subplot(y_index+index),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(titles[index]), plt.xticks([]), plt.yticks([])



img = cv2.imread("./images/edgeDetection.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#canny edge detection
canny_edges = cv2.Canny(img,100,200)

#laplacian edge detection
laplacian_edges = cv2.Laplacian(gray_img,cv2.CV_8U)

#Edge detect inside edge detection(canny to laplacian)
canny_to_laplacian = cv2.Laplacian(canny_edges,cv2.CV_8U)

#same as above, but other way around
laplacian_to_canny = cv2.Canny(laplacian_edges,100,200)

images = [img, gray_img, canny_edges, laplacian_edges, canny_to_laplacian, laplacian_to_canny]
titles = ['Original Image', 'Gray level Image', 'Canny Image', 'Laplacian Image', 'Canny -> Laplacian','Laplacian -> Canny']

ploterFunction(images, titles, 321)

plt.show()


