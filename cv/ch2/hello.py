# coding: utf-8 
# create by cgr  2019/8/23
import tensorflow as tf
hello = tf.constant('hello tf')
sess = tf.Session()
print (sess.run(hello))

import cv2
print ('hello cv')