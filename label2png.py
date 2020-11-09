import cv2 as cv
import numpy as np
import random
import scipy.io
name ='table'
mat_f ="C:/Users/Jo/PycharmProjects/LFprocess/mat/"+name+".mat"
#mat_f= "C:/Users/Jo/PycharmProjects/LFprocess/zzz/lightfieldsuperpixels-master/lightfieldsuperpixels-master/results/24-Sep-2020_2232hrs/scene20.mat"
mat_fn=scipy.io.loadmat(mat_f)
print("STAGE 0 LABEL Visualization")
number_of_colors = 2000
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(len(set(color)))
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


img = cv.imread("C:/Users/Jo/PycharmProjects/LFprocess/10_30/image.png")
w,h,c=img.shape
print( w,h,c)
label = np.zeros((w, h, 1), np.uint8)
out_img = np.zeros((w, h, 3), np.uint8)
f = open("C:/Users/Jo/PycharmProjects/LFprocess/10_30/11_1/label.txt", 'r')
lines= f.readlines()

for v in range(9):
    for u in range(9):
        out_img = np.zeros((h, w, 3), np.uint8)
        for y in range(h):
            for x in range(w):
                c_idx = color[int(mat_fn['X'][y][x][v][u])]
                # c_idx = int(mat_fn['X'][y][x][v][u]) % 256
                out_img[y][x] = hex_to_rgb(c_idx)
        cv.imwrite('C:/Users/Jo/PycharmProjects/LFprocess/10_30/lb_map/' + str(v) + "_" + str(u) + "_mat.png", out_img)

for i,line in enumerate(lines):
    y=int(i/h)
    x=int(i%w)
    label[y][x]=line
    #print(i ,line)
f.close()

for i in range(h):
    for j in range(w):
        #print(i,j,label[i][j])
        c_idx = color[int(label[i][j])]
        # c_idx = int(mat_fn['X'][y][x][v][u]) % 256
        out_img[i][j] = hex_to_rgb(c_idx)
    cv.imwrite('./label_map.png', out_img)
print(len(label))