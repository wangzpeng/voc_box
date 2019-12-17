import os
import cv2
import numpy as np

f=open('color.txt','a+')
for img_name in os.listdir("./JPEGImages/"):
	img=cv2.imread("./JPEGImages/"+img_name,cv2.IMREAD_GRAYSCALE)
	hist,bins=np.histogram(img.ravel(),bins=10)
	f.write(img_name+' '+str(hist)+'\n')

f.close()
