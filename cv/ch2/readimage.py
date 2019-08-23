# coding: utf-8
# create by cgr  2019/8/23
import cv2
# 1文件读取 2 封装格式解析 3 数据解码 4数据加载
img = cv2.imread('image0.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)