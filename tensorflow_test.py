#-*- coding:utf-8 -*-
__author__ = 'tony'
import tensorflow as tf

# hello = tf.constant('hello,TensFlow')
# sess = tf.Session()
# print(sess.run(hello))
# a = tf.constant(10)
# b = tf.constant(32)
# print(sess.run(a+b))

# hello = tf.constant(
#     'Hello, TensorFlow!'
# )
# sess = tf.Session()
# print (sess.run(hello))

a = tf.constant(2)
b = tf.constant(3)
with tf.Session() as sess:
    print('a=2,b=3')
    print('Addition with constants:%i')%sess.run(a+b)
    print('Multipliction with constants:%i')%sess.run(a*b)
