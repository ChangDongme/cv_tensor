# coding: utf-8 
# create by cgr  2019/8/23
import cv2


img_form ='png'
## ->>jpg
# 1M 100k 10k    0-100有损压缩
if 'jpg' == img_form:
    img = cv2.imread('image1.jpg', 1)
    print('this is jpg')
    cv2.imwrite('image1Test2.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,50])


## ->> png
#无损 透明度属性
if 'png' == img_form:
    print('this is png')
    img = cv2.imread('img_png0.png', 1)
    # jpg 0压缩比稿  0-100;    png 0 压缩比低 0-9
    cv2.imwrite('img_png0-1.png',img,[cv2.IMWRITE_PNG_COMPRESSION,99])

