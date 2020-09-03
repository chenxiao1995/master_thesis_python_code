import os
import sys
prefix = 'TFH_'
path="/Users/xiao/Desktop/20200603_Testfahrt/TFH_label/"
def add_prefix_files(prefix,path):             #定义函数名称
    old_names = os.listdir(path)  #取路径下的文件名，生成列表
    for old_name in old_names:      #遍历列表下的文件名
            if  old_name!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
               if old_name.endswith('.xml'):   #当文件名以.txt后缀结尾时
                    os.rename(os.path.join(path,old_name),os.path.join(path,prefix+old_name))  #重命名文件
                    print (old_name,"has been renamed successfully! New name is: ",prefix+old_name)  #输出提示


if __name__ == '__main__':
    try:
        add_prefix_files(prefix,path)
    except SystemExit:
        pass
