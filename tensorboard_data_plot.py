import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os

path="/Users/xiao/Desktop/python_skript/tensorflowboard_data"
'''read csv file'''
def readcsv(file):
    file_path=os.path.join(path,file)
    csvfile=open(file_path,'r')
    plots=csv.reader(csvfile,delimiter=',')
    x=[]
    y=[]
    '''skip the head'''
    next(plots)
    for row in plots:
        x.append(int(row[1])/1000)
        y.append(float(row[2]))
    return x,y


plt.figure()

x1,y1=readcsv("run-bs_64_da_def_lr_4e-03_eval_0-tag-loss.csv")
print(y1)
plt.plot(x1,y1,color='red',label='default')

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.ylim(0,16)
plt.xlim(0,35)
plt.xlabel('x1000 Schritt',fontsize=20)
plt.ylabel('Loss',fontsize=20)
plt.legend(fontsize=16)
plt.show()
plt.savefig('test.png')