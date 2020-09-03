import os
import shutil
path_to="/Volumes/xiao_ssd/20200813_testdaten/a_zone/a_zone3/image/"
path_from="/Volumes/xiao_ssd/20200813_testdaten/a_zone/a6_image"
# label_path="/Volumes/xiao_ssd/Masterarbeit/TF_H_N/label/"
# for root,dirs,files in os.walk(img_path):
#     for file in files:
#         src_file=os.path.join(root,file)
#         shutil.copy(src_file,path)
#         print(file)
# for path,d,filelist in os.walk(img_path):
#     for filename in filelist:
#         suffix=os.path.splitext(filename)[-1]
#         src=os.path.join(path,filename)
#         if suffix == '.png':
#             dst=os.path.join(img_path,filename)
#             shutil.copy(src, dst)
#         elif suffix == '.xml':
#             dst=os.path.join(label_path,filename)
#             shutil.copy(src, dst)
def copy_all_file(path_from,path_to):
    for root,dirs,files in os.walk(path_from):
        for file in files:
            file_path=os.path.join(root,file)
            shutil.copy(file_path,path_to)

if __name__=='__main__':
    copy_all_file(path_from,path_to)

