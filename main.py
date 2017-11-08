import cv2
from matplotlib import pyplot as plt
import numpy as np

im = cv2.imread('img/monyet.jpg')
# print(im.shape)
# cv2.imshow('ORIGINAL',im)
# cv2.waitKey(0)

#RGB TO GRAY
r = im[:,:,2]
g = im[:,:,1]
b = im[:,:,0]

(b1,g1,r1) =cv2.split(im)
gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
# cv2.imshow('ORIGINAL',im)
# cv2.waitKey(0)

# ori =cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
# cv2.imshow('ORIGINAL',ori)
# cv2.waitKey(0)

#COLOR HISTOGRAM
color = ('b','g','r')
for i,colo in enumerate(color):
    hist = cv2.calcHist([im],[i],None,[256],[0,256])
    plt.xlim([0,256])
# plt.hist(hist)
# plt.show()

#ROTATING
(h,w) = im.shape[:2]
# print(h,w)

center = (w/2,h/2)
# print(center)

# M =cv2.getRotationMatrix2D(center,90,1.0)
# rotated = cv2.warpAffine(im,M,(h,w))
# cv2.imshow('Rotation',rotated)
# cv2.waitKey(0)

#CROPING
cropped = im[250:430,450:770]
# cv2.imshow('Cropping',cropped)
# cv2.waitKey(0)

#Edge & SHARPENING & BLUR
edge = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),dtype="int")
sharp = np.array(([0,-1,0],[-1,5,-1],[0,1,0]),dtype="int")
blur = np.array(([1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]))
convlution = cv2.filter2D(im,-1,sharp)
# cv2.imshow('SHARPENING',convlution)
# cv2.waitKey(0)

plt.subplot(121),plt.imshow(im),plt.title('ORIGINAL')
plt.subplot(122),plt.imshow(convlution),plt.title('SHARP')
plt.show()