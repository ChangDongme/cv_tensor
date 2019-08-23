# coding: utf-8 
# create by cgr  2019/8/23
import cv2

img = cv2.imread('image1.jpg',1)
(b,g,r) =img[100,100]

print(b,g,r)

# 10 100 -- 110 100

for i in range(0,100):
    img[10+i,100] = (255,0,0) ##b g r 标准蓝色
    img[100,10+i] = (0,255,0)
cv2.imshow('image',img)
cv2.waitKey(0)
