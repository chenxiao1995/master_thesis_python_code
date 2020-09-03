import os, random, shutil
image_path='/Volumes/xiao_ssd/Masterarbeit/TF_H_N/image/'
label_path='/Volumes/xiao_ssd/Masterarbeit/TF_H_N/label/'

train_path='/Volumes/xiao_ssd/Masterarbeit/RF04/train/'
val_path='/Volumes/xiao_ssd/Masterarbeit/RF04/val/'
# test_path='/Volumes/xiao_ssd/Masterarbeit/RF01/test/'

train_ratio=0.85
val_ratio=0.15
# test_ratio=0.15

def move_file(src_path,dst_path,filename,ord="image"):
    f_src=os.path.join(src_path,filename)
    f_dst=os.path.join(dst_path,ord,filename)
    shutil.copy(f_src,f_dst)

image_name_list=os.listdir(image_path)
random.shuffle(image_name_list)
image_n=len(image_name_list)
train_n=round(image_n * train_ratio)
val_n=round(image_n*val_ratio)

train_name=image_name_list[:train_n]
val_name=image_name_list[train_n:]

# val_name=image_name_list[train_n:train_n+val_n]
# tesl_name=image_name_list[train_n+val_n:]

print(len(train_name))
print(len(val_name))
# print(len(tesl_name))

for name in train_name:
    label_name=name.split('.')[0]+'.xml'
    move_file(image_path,train_path,name,ord="image")
    move_file(label_path,train_path,label_name,ord="label")

for name in val_name:
    label_name=name.split('.')[0]+'.xml'
    move_file(image_path,val_path,name,ord="image")
    move_file(label_path,val_path,label_name,ord="label")

# for name in tesl_name:
#     label_name=name.split('.')[0]+'.xml'
#     move_file(image_path,test_path,name,ord="image")
#     move_file(label_path,test_path,label_name,ord="label")

