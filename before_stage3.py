import cv2 as cv
import scipy.io
import numpy as np
import os
name='table'
mat_f ="C:/Users/Jo/PycharmProjects/LFprocess/mat/"+name+".mat"
#mat_f= "C:/Users/Jo/PycharmProjects/LFprocess/zzz/lightfieldsuperpixels-master/lightfieldsuperpixels-master/results/24-Sep-2020_2232hrs/scene20.mat"
mat_fn=scipy.io.loadmat(mat_f)
width =512#512#768
height=512 #512#768
cent_v=4
cent_u=4
label_num = []
hex_=dict()
img =cv.imread("C:/Users/Jo/PycharmProjects/LFprocess/mat/table/10_26/lamp.png")
with open("C:/Users/Jo/PycharmProjects/LFprocess/mat/table/10_26/label.txt",'r') as file:
    for i,txt in enumerate(file):

        hex_[txt.strip('\n')]=i+1# label 은 1번부터인가?
print(hex_)

def rgb2hex2label(r,g,b):
    hex_s = format(int(r),'X')+format(int(g),'X')+format(int(b),'X')
    return int(hex_[hex_s])

img1= img[0:512,9:521]
img2 = img[0:512,527:1039]
cv.imwrite("d.png",img1)
cv.imwrite("a.png",img2)

#TODO --1 LOAD LABEL



#TODO 3 Indirect Guide

im=cv.imread('d.png',0)

im2=cv.imread('C:/Users/Jo/PycharmProjects/LFprocess/mat/table/10_26/nobook.png',0)
im3 = cv.absdiff(im,im2)
ret,out=cv.threshold(im3,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
cv.imwrite("C:/Users/Jo/PycharmProjects/LFprocess/mat/table/10_26/diff_guide.png",im3)
cv.imwrite("C:/Users/Jo/PycharmProjects/LFprocess/mat/table/10_26/Id_mask.png",out)

Guide = np.empty((1, 2), dtype=int)
w,h = out.shape[:]
print (w,h)
Ind_guide = []
#mask 위치 찾기

for x in range(w):
    for y in range(h):
        if out[y][x] > 0:
            item = np.array([[x, y]])
            Guide = np.append(Guide, item, axis=0)

#mask label찾기
for pix in Guide[1:]: # x=[0] y =[1]
    y=int(pix[1])
    x=int(pix[0])
    # B G R
    try:
        Ind_guide.append(rgb2hex2label(img2[y][x][2],img2[y][x][1],img2[y][x][0]))
    except:
        print("except")
        hex_s = format(int(img2[y][x][2]), 'X') + format(int(img2[y][x][1]), 'X') + format(int(img2[y][x][0]), 'X')
        print (hex_s)
   #Ind_guide.append(int(mat_fn['N'][y][x][cent_v][cent_u]))
ind_gd=list(set(Ind_guide))
print(ind_gd)
#mat에서 label만 1 나머진 0

for v in range(9):
    for u in range(9):
        out_img = np.zeros((height, width, 1), np.uint8)
        for y in range(height):
            for x in range(width):
                if int(mat_fn['X'][y][x][v][u]) in ind_gd:
                    out_img[y][x]=255
        cv.imwrite('C:/Users/Jo/PycharmProjects/LFprocess/mat/'+name+'/f_mask/'+str(v) + "_" + str(u) + "_mask.png", out_img,[cv.IMWRITE_PNG_BILEVEL,1])
