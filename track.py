import sys

import cv2
print cv2.__version__
scale = 1
delta = 0
ddepth = cv2.CV_16S
# needed for orb because of a bug
#cv2.ocl.setUseOpenCL(False)

import lktrack
import glob
import numpy as np

img_array = []

direc = './data/'
for i in range(108):
    #fileName = direc + 'image00' + str(i+1) +'.jpg'
    fileName = direc + 'img' + str(i+1) +'.jpg'
    img_array.append(fileName)
    
#print img_array[0]
print "length ", len(img_array)
imgA = img_array[40:80]
print imgA
lkt = lktrack.LKTracker(imgA)
lkt.detect_points()




image = cv2.imread(imgA[0])
#lkt.image = image
#lkt.gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#lkt.prev_gray = lkt.gray


#for point in initial_points:
    #print point
#    cv2.circle(image,(int(point[0]),int(point[1])),3,(0,255,0),-1)

cv2.imshow('LKtrack',image)
lkt.draw()
#cv2.waitKey()

for i in range(len(imgA)-1):
    lkt.track_points()
    #lkt.draw()
    lkt.write()
    
#cv2.destroyAllWindows()

