# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
#指明被遍历的文件夹
a = input('本程序工作目录为C:png\n请输入需要截图的左坐标a')
b = input('请输入需要截图的上坐标b')
c = input('请输入需要截图的右坐标c')
d = input('请输入需要截图的下坐标d')
rootdir = r'C:\Users\17\Desktop\56565656\png'
for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
   
        img = Image.open(currentPath)
        print (img.format, img.size, img.mode)
        #img.show()
        box1 = (500, 600,800, 900)#设置左、上、右、下的像素
        image1 = img.crop(box1) # 图像裁剪
        image1.save(r'C:\Users\317\Desktop\56565656\png'+'\\'+filename) #存储裁剪得到的图像5
