'''import cv2
import numpy as np
import h5py

f = h5py.File('C:/Users/Jo/Desktop/scene.h5','r')
one_data= f['key']
print(one_data)'''

# -*- coding: utf-8 -*-
# Created by:
#Author :Hasan Latif
#Email :hasanlatif.pk@gmail.com
# WARNING! All changes made in this file will be lost!
# for using this code you need opencv,h5py.
# for installing just use the pip

p3="C:/Users/Jo/Desktop/HCI-dataset-Copy/blender/stillLife/dpeth/"
p2= "C:/Users/Jo/Desktop/HCI-dataset-Copy/blender/papillon/feature_gt_depth_probabilities.h5"
import cv2
import numpy as np
import h5py
import time
name= 'stillLife'
#path='C:/Users/Jo/Desktop/HCI-dataset-Copy/blender/'+name+'/lf.h5'
def read_dataset(path, flag):
    print("[Info]>>Starts at",time.ctime())
    hf = h5py.File(path, 'r')

    if(flag=='Probabilities'):
        get_flag = hf.get('Probabilities')
        print(get_flag)
        np_array=np.array(get_flag)
        for row in range(0, 9):
            for col in range(0, 9):
                n1 = np_array[:, :, :][:, :, :][row][col]
                print(n1)
                #n1 = np_array[:,][:,][row][col]
                n1=cv2.cvtColor(n1,cv2.COLOR_RGB2BGR)
                print("[info]>> Writing stillLife-{}-{} .png".format(str(row), str(col)))
                cv2.imwrite(p3+name+'-'+str(row)+'-'+str(col)+'.png',n1)

        print("[Info]>>Ends at", time.ctime())




if __name__ == '__main__':

    read_dataset(p2,'Probabilities')
