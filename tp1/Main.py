#TP1 Matthieu Caron

import tensorflow as tf
import numpy as np
import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

############# Usefull functions #################
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

#################### Defining size of input and output ####################
# Define the size of the input and of the output
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

#################### Building the DNN #####################
########## Declaring weights of layer 1 and 2 ##########
# Layer 1
W1 = weight_variable([784,10])
b1 = bias_variable([10])

#################### Defining the loss #####################
# Loss cross entropy
cross_entropy = - tf.reduce_sum(y_ * tf.log(y_out))