import os
import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
csv_path="/Volumes/xiao_ssd/Masterarbeit/RF04/data/test_labels.csv"
csv_pd=pd.read_csv(csv_path)
print(csv_pd['class'].value_counts())
csv_pd['class']=csv_pd['class'].replace({'walker':'walking stick','crutches':'walking frame'})
print(csv_pd['class'].value_counts())
csv_pd.to_csv("test_labels_out.csv",index=False,sep=',')