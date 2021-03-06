import numpy as np
import argparse
from matplotlib import pyplot as plt
import cv2

#Loading the image and turning it into gray level
img = cv2.imread("./images/phaseTest.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft[dft == 0] = 0.0000001

magnitude, phase = 20*np.log(cv2.cartToPolar(dft[:,:,0],dft[:,:,1]))

#Defining some aux variables
width, height = img.shape[:2]
amp_to_phase = np.zeros((width,height,2))

#convert it back
amp_to_phase[:,:,0], amp_to_phase[:,:,1] = cv2.polarToCart(magnitude, phase)

#ploting (no aux func this time)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(phase, cmap = 'gray')
plt.title('Phase '), plt.xticks([]), plt.yticks([])
plt.show()

# mouse events for the image
def on_mouse_click_event(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		img = cv2.imread("./images/phaseTest.jpg")
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		img2 = img.copy()

		cv2.imshow("Image2", img)

		dft = cv2.dft(np.float32(img2),flags = cv2.DFT_COMPLEX_OUTPUT)
		#Avoid the warning of log 0
		dft[dft == 0] = 0.0000001

		#Take the magnitude and phases
		magnitudeWindow, phaseWindow = 20*np.log(cv2.cartToPolar(dft[:,:,0],dft[:,:,1]))

		#Apply some edge detection on the image
		img2 = cv2.Canny(img2,100,200)


		cv2.imshow("Spacial", img2)
		cv2.imshow("Magnitude", magnitudeWindow)
		cv2.imshow("Phase", phaseWindow)

		img2 = img2[img2>150]
		magnitudeWindow = magnitudeWindow[magnitudeWindow>150]
		phaseWindow = phaseWindow[phaseWindow>150]

		#Print info
		print('Window edges = ',img2.size)
		print('Magnitude edges = ',magnitudeWindow.size)
		print('Phase edges = ',phaseWindow.size)
		
		print('Click on the image or press ENTER to exit\n')

cv2.namedWindow('Image2')

cv2.setMouseCallback('Image2',on_mouse_click_event)

#helper info
print('Click on the image or press ENTER to exit\n')

#Program loop
while(1):
	cv2.imshow('Image2',img)
	k = cv2.waitKey(0)
	if k:
		break

#exit
cv2.destroyAllWindows()
		