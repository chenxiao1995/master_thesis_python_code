# coding=utf-8
# This file is used to extract the training log, remove the unresolvable log and format the log file, and generate a new log file for the visualization tool to draw.

import inspect
import os
import random
import sys

path='/Users/xiao/Downloads/'

def extract_log(log_file, new_log_file, key_word):
    with open(path+log_file, 'r') as f:
        with open(path+new_log_file, 'w') as train_log:
            # f = open(log_file)
            # train_log = open(new_log_file, 'w')
            for line in f:
                # Remove moregpuSynchronization log
                if 'Syncing' in line:
                    continue
                # Remove log of zero error
                if 'nan' in line:
                    continue
                if key_word in line:
                    train_log.write(line)
    f.close()
    train_log.close()


extract_log('train0830.log', 'train_log_loss.txt', 'images')
extract_log('train0830.log', 'train_log_iou.txt', 'IOU')