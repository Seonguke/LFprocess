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
img =cv.imread("C:/Users/Jo/PycharmProjects/LFprocess/10_30/11_1/image2.png")
with open("C:/Users/Jo/PycharmProjects/LFprocess/10_30/11_1/label2.txt",'r') as file:
    for i,txt in enumerate(file):

        hex_[txt.strip('\n')]=i# label 은 1번부터인가?
print(hex_)

def rgb2hex2label(r,g,b):
    hex_s = format(int(r),'X')+format(int(g),'X')+format(int(b),'X')
    return int(hex_[hex_s])



#TODO --1 LOAD LABEL

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

im=cv.imread('C:/Users/Jo/PycharmProjects/LFprocess/10_30/11_1/image2.png')
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
    draw_label.append(rgb2hex2label(img[y][x][2],img[y][x][1],img[y][x][0]))

#mat에서 label만 1 나머진 0
for v in range(9):
    for u in range(9):
        out_img = np.zeros((height, width, 1), np.uint8)
        for y in range(height):
            for x in range(width):
                if int(mat_fn['X'][y][x][v][u]) in draw_label:
                    out_img[y][x]=255
        cv.imwrite(
            'C:/Users/Jo/PycharmProjects/LFprocess/mat/' + name + '/f_mask/' + str(v) + "_" + str(u) + "_mask.png",
            out_img, [cv.IMWRITE_PNG_BILEVEL, 1])

#TODO 3 Indirect Guide
