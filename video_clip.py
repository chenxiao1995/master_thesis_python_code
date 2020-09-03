import os
import cv2

data_path='/Volumes/xiao_ssd/data/frontview'
cut_frame = 60

for root, dirs, files in os.walk(data_path):
    for file in files:
        img_num=0
        dir_path=os.path.join(data_path,file.split('.')[0])
        video_path=os.path.join(data_path,file)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        video=cv2.VideoCapture(video_path)
        video_fps = int(video.get(cv2.CAP_PROP_FPS))
        print('current video fps is: {}'.format(video_fps))
        current_frame=0
        while(True):
            ret,image=video.read()
            current_frame+=1
            if ret is False:
                video.release()
                break
            if current_frame%cut_frame==0:
                cv2.imwrite(dir_path+'/'+file.split('.')[0]+'_'+str(img_num)+'.png',image)
                img_num+=1
        print('Saving'+file+'in'+str(img_num)+' image')



