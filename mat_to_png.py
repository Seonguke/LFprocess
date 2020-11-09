import numpy as np
import matplotlib.pylab as plt
import scipy.io
import cv2 as cv
import random
import os
import pandas as pd
name='table'
mat_f ="C:/Users/Jo/PycharmProjects/LFprocess/mat/"+name+".mat"
#mat_f= "C:/Users/Jo/PycharmProjects/LFprocess/zzz/lightfieldsuperpixels-master/lightfieldsuperpixels-master/results/24-Sep-2020_2232hrs/scene20.mat"
mat_fn=scipy.io.loadmat(mat_f)
width =512#768#512#768
height=512#768 #512#768
cent_v=4
cent_u=4

#TODO 0 시각화하기
path='C:/Users/Jo/Desktop/h5_jpg/'
mat_f ="C:/Users/Jo/Desktop/scene20.mat"

for v in range(9):
    for u in range(9):
        out_img = np.zeros((height* width), np.uint16)
        out_img2 = np.zeros((height, width, 3), np.uint8)
        cnt =0
        for y in range(height):
            for x in range(width):
                # c_idx = int(mat_fn['X'][y][x][v][u]) % 256
                out_img[cnt] = mat_fn['X'][y][x][v][u]
                cnt=cnt+1
                #print( mat_fn['N'][y][x][v][u])
        print(out_img)
        df=pd.DataFrame(out_img)
        df.to_csv('C:/Users/Jo/PycharmProjects/LFprocess/mat/table/label/'+ str(v) + "_" + str(u) + "_mat.csv",header=None,index=None)
        #cv.imwrite('C:/Users/Jo/Desktop/'+name+'/'+'real_label/' + str(v) + "_" + str(u) + "_mat.png", out_img)


