import cv2
import os

if __name__=='__main__':
    sourceDir='/Volumes/xiao_ssd/data/data/TFH/img/'
    resultDir='/Volumes/xiao_ssd/data/data/TFH_downsize/img/'

    img_list=os.listdir(sourceDir)

    # img_test_path='/Volumes/xiao_ssd/data/data/TFH/img/TFH_17.png'
    # pic_test=cv2.imread(img_test_path,cv2.IMREAD_COLOR)
    # pic_test_resize=cv2.resize(pic_test,(640,360))
    # print(pic_test_resize.shape)
    # cv2.imshow('figure',pic_test_resize)
    for i in img_list:
        pic=cv2.imread(os.path.join(sourceDir,i),cv2.IMREAD_COLOR)
        pic_resize=cv2.resize(pic,(640,360))
        cv2.imwrite(os.path.join(resultDir,i),pic_resize)