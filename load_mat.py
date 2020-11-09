import numpy as np
import matplotlib.pylab as plt
import scipy.io
import cv2 as cv
import random
import os
name='stillLife'
#mat_f ="C:/Users/Jo/PycharmProjects/LFprocess/zzz/lightfieldsuperpixels-master/lightfieldsuperpixels-master/results/VCLFS/"+name+"20.mat"
mat_f ="C:/Users/Jo/PycharmProjects/LFprocess/mat/table.mat"

#mat_f= "C:/Users/Jo/PycharmProjects/LFprocess/zzz/lightfieldsuperpixels-master/lightfieldsuperpixels-master/results/24-Sep-2020_2232hrs/scene20.mat"
mat_fn=scipy.io.loadmat(mat_f)
#print(mat_fn)
width =512#512#768
height=512 #512#768
cent_v=4
cent_u=4
'''
#TODO 0 시각화하기
print("STAGE 0 LABEL Visualization")
number_of_colors = 2000
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(len(set(color)))    
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

path='C:/Users/Jo/Desktop/h5_jpg/'
for v in range(9):
    for u in range(9):
        out_img = np.zeros((height, width, 3), np.uint8)
        for y in range(height):
            for x in range(width):
                c_idx = color[int(mat_fn['X'][y][x][v][u])]
                # c_idx = int(mat_fn['X'][y][x][v][u]) % 256
                out_img[y][x] = hex_to_rgb(c_idx)
        cv.imwrite('./label/' + str(v) + "_" + str(u) + "_mat.png", out_img)
'''
#TODO 1 Drawing MASk  뽑기
print("STAGE 1 Drawing MASK")
#path ='C:/Users/Jo/Desktop/h5_jpg/'+str(cent_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 v)+'_'+str(cent_u)+'_mat.png'
# 마우스 콜백 함수: 연속적인 원을 그리기 위한 콜백 함수
arr = np.empty((1, 2), dtype=int)
def DrawConnectedCircle(event, x, y, flags, param):
    global drawing,arr
    # 마우스 왼쪽 버튼이 눌리면 드로윙을 시작함
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        cv.circle(im, (x, y), 2, (255, 255, 255), -1)
        item = np.array([[x, y]])
        arr = np.append(arr, item, axis=0)
        print(x, y)

    # 마우스가 왼쪽 버튼으로 눌린 상태에서 마우스 포인트를 움직이면
    # 움직인 자취를 따라서 마우스의 점들이 그려짐
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(im, (x, y), 2, (255, 255, 255), -1)
            print(x, y)
            item = np.array([[x, y]])
            arr = np.append(arr, item, axis=0)
    # 마우스 왼쪽 버튼을 떼면 드로윙을 종료함
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


drawing = False  # 마우스 왼쪽 버튼이 눌러지면 그리기 시작

im=cv.imread('./label/4_4_mat.png')
cv.namedWindow('image')
cv.setMouseCallback('image', DrawConnectedCircle)

while (1):
    cv.imshow('image', im)
    k = cv.waitKey(1) & 0xFF

    if k == 27:
        print(arr)
        break
print(len(arr))
cv.destroyAllWindows()

#TODO 2 80개 한꺼번에 뽑기
print("Stage 3 Gen 81 Mask")
draw_label=[]
#색칠한 label 담아 놨다.
for pix in arr[1:]: # x=[0] y =[1]
    y=int(pix[1])
    x=int(pix[0])
    draw_label.append(int(mat_fn['X'][y][x][cent_v][cent_u]))

#mat에서 label만 1 나머진 0
for v in range(9):
    for u in range(9):
        out_img = np.zeros((height, width, 1), np.uint8)
        for y in range(height):
            for x in range(width):
                if int(mat_fn['X'][y][x][v][u]) in draw_label:
                    out_img[y][x]=255
        cv.imwrite('./mask/'+str(v) + "_" + str(u) + "_mask.png", out_img,[cv.IMWRITE_PNG_BILEVEL,1])
        """
#TODO 3 Indirect Guide
im=cv.imread('C:/Users/Jo/Desktop/stillLife/original/stillLife-4-4.jpg',0)
im2=cv.imread('C:/Users/Jo/Desktop/stillLife/4_4.png',0)
im3 = cv.absdiff(im,im2)
ret,out=cv.threshold(im3,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
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
    Ind_guide.append(int(mat_fn['N'][y][x][cent_v][cent_u]))

#mat에서 label만 1 나머진 0
for v in range(9):
    for u in range(9):
        out_img = np.zeros((height, width, 1), np.uint8)
        for y in range(height):
            for x in range(width):
                if int(mat_fn['N'][y][x][v][u]) in Ind_guide:
                    out_img[y][x]=255
        cv.imwrite('C:/Users/Jo/Desktop/'+name+'/'+str(v) + "_" + str(u) + "_mask.png", out_img,[cv.IMWRITE_PNG_BILEVEL,1])"""