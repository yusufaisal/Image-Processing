import cv2
from matplotlib import pyplot as plt

im = cv2.imread('img/monyet.jpg')

print(im.shape)

# cv2.imshow('ORIGINAL',im)
# cv2.waitKey(0)

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

color = ('b','g','r')
for i,colo in enumerate(color):
    hist = cv2.calcHist([im],[i],None,[256],[0,256])
    plt.xlim([0,256])
# plt.hist(hist)
# plt.show()

(h,w) = im.shape[:2]
# print(h,w)

center = (w/2,h/2)
# print(center)

# M =cv2.getRotationMatrix2D(center,90,1.0)
# rotated = cv2.warpAffine(im,M,(h,w))
# cv2.imshow('Rotation',rotated)
# cv2.waitKey(0)

cropped = im[250:430,450:770]
cv2.imshow('Cropping',cropped)
cv2.waitKey(0)
