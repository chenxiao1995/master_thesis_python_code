import urllib
import cv2
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers
AUTOTUNE = tf.data.experimental.AUTOTUNE

import PIL.Image

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 5)
from numpy import average,dot,linalg
import numpy as np

def visualize(original, augmented):
  fig = plt.figure()
  plt.subplot(1,2,1)
  plt.title('Original image')
  plt.imshow(original)

  plt.subplot(1,2,2)
  plt.title('Augmented image')
  plt.imshow(augmented)

def cos_similarity(image1,image2):
  '''

  :param image1:shape=?,?,3
  :param image2:shape=?,?,3
  :return: cosine similarity
  '''
  #
  images = [image1, image2]
  vectors = []
  norms = []
  for image in images:
    vector = []
    for pixel_tuple in image:
      vector.append(average(pixel_tuple))
    vectors.append(vector)
    # linalg=linear（线性）+algebra（代数），norm则表示范数
    # 求图片的范数？？
    norms.append(linalg.norm(vector, 2))
  a, b = vectors
  a_norm, b_norm = norms
  # dot返回的是点积，对二维数组（矩阵）进行计算
  res = dot(a / a_norm, b / b_norm)
  return res

  # return cos



image_path="/Volumes/xiao_ssd/data/data/TFH/img/TFH_176.png"
# PIL.Image.open(image_path)
image=plt.imread(image_path)
# plt.imshow(image)
# plt.show()
image_string=tf.io.read_file(image_path)
image_org=tf.image.decode_png(image_string,channels=3)
print(image_org)
image_flip_left_right = tf.image.flip_left_right(image_org)
image_resize_1=tf.image.resize(image_org,[380,640],method=1)
image_resize_2=tf.image.resize(image_org,[300,300],method=1)
image_resize_3=tf.image.resize(image_resize_1,[300,300],method=1)
# visualize(image,flipped)
# plt.show()
with tf.Session() as sess:
  # # image_o=image_org.eval()
  # # image_a=image_resize.eval()
  image_o=image_org.eval()
  image_1=image_resize_1.eval()
  image_2=image_resize_2.eval()
  image_3=image_resize_3.eval()
  # diff_image=image_2-image_3
  # print(diff_image.shape)
  # plt.imshow(diff_image)
  # # plt.show()

  visualize(image_o,image_1)
  visualize(image_2,image_3)
  plt.show()

# plt.imshow(image)
# flipped = tf.image.flip_left_right(image)
# visualize(image, flipped)