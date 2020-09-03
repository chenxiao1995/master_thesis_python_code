import os
import glob
from shutil import copy

key="a6"
path="/Volumes/xiao_ssd/20200813_testdaten/a_zone"
img_path_all=os.path.join(path,key)
img_path=os.path.join(path,key+'_image')
label_path=os.path.join(path,key+'_label')

def find_img_file_with_obj(label_path,image_path_from,image_path_to):
    if not os.path.exists(image_path_to):
        os.mkdir(image_path_to)
    for file in glob.glob(label_path+'/*.xml'):
        file_name=file.split('/')[-1]
        img_file_name=file_name.split('x')[0]+'png'
        #print(img_file_name)
        file_from=os.path.join(image_path_from,img_file_name)
        copy(file_from,image_path_to)

if __name__ == '__main__':
    try:
        find_img_file_with_obj(label_path,img_path_all,img_path)
    except SystemExit:
        pass