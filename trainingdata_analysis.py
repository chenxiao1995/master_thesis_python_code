import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd

img_bg='/Users/xiao/Desktop/snapshot_2019_07_30_10_11_11.jpg'
csv_path='/Volumes/xiao_ssd/data/RF01/data/'
data=pd.read_csv(csv_path+'train_label.csv')
print("The total number of the object is",data.shape[0])
# data['class'].hist(grid=False,figsize=(8,6),bins=
data['x_c']=(800/data['width'])*(data['xmin']+data['xmax'])/(2)
data['y_c']=(450/data['height'])*(data['ymin']+data['ymax'])/(2)
data['alpha']=abs(data['ymax']-data['ymin'])/abs(data['xmax']-data['xmin'])
print(data.head(5))
data['alpha'].hist(bins=[0:0.1:5])
plt.show()
# data_class=data.groupby(by="class").count()
# fig1,ax1=plt.subplots()
# ax1.invert_yaxis()
# img=Image.open(img_bg)
# plt.imshow(img.resize((800,450)))
# plt.scatter(data['x_c'],data['y_c'],s=(1,),alpha=0.4)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Verteilung der Mittelpunkte der Objekte')
#
# # fig2,ax2=plt.subplots()
# # plt.hist(data['alpha'],bins=30)
# # data['alpha'].hist(grid=False,figsize=(8,6),bins=10)
# plt.show()
