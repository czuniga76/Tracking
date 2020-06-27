import cv2
print cv2.__version__
scale = 1
delta = 0
ddepth = cv2.CV_16S
# needed for orb because of a bug
#cv2.ocl.setUseOpenCL(False)

import lktrack
import numpy as np
import matplotlib.pyplot as plt


img_array = []

direc = './data/R2Img/'
for i in range(108):
    fileName = direc + 'img' + str(i+1) +'.jpg'
    img_array.append(fileName)
    
#print img_array[0]
print "length ", len(img_array)
imgA = img_array[40:80]

lkt = lktrack.LKTracker(imgA)
for im,ft in lkt.track():
    print 'tracking %d features' % len(ft)
    plt.figure()
    plt.imshow(im)
    for p in ft:
        plt.plot(p[0],p[1],'bo')
    for t in lkt.tracks:
        plt.plot([p[0] for p in t],[p[1] for p in t])
    plt.axis('off')
    plt.show()
        