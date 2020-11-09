import cv2
import numpy as np
im=cv2.imread('C:/Users/Jo/Desktop/stillLife/original/stillLife-4-4.jpg',0)

im2=cv2.imread('C:/Users/Jo/Desktop/stillLife/4_4.png',0)
def sel(image):
    saliency = cv2.saliency.StaticSaliencyFineGrained_create()
    (sucess, saliencymap) = saliency.computeSaliency(image)
    saliencymap = (saliencymap * 255).astype("uint8")
    return saliencymap
img = sel(im)
img2 = sel(im2)


im3 = cv2.absdiff(im,im2)

ret,out=cv2.threshold(im3,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

seli = sel(out)
ths=cv2.threshold(seli.astype("uint8"),50,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]

cv2.imshow('asd',im3)
cv2.imshow('h',out)

print(out)
cv2.imshow('zz',seli)
cv2.imshow('xx',ths)
#print(set(im3))
cv2.waitKey(0)