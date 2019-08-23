# coding: utf-8 
# create by cgr  2019/8/23
#学习TensorFlow  类比编程语言
#类比 语法 api  原理
## 基础数据类型, 运算符  流程 字典  数组


import tensorflow as tf

## 定义常量

data1 = tf.constant(2,dtype=tf.int32)
data2 = tf.Variable(10,name='var')
print(data1)
print(data2)

session = tf.Session()
print(session.run(data1))
init = tf.global_variables_initializer()
session.run(init)
print(session.run(data2))