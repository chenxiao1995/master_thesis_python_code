import tensorflow as tf
import matplotlib.pyplot as plt

steps=[]
loss=[]
mAP=[]
steps_val=[]
loss_val=[]
mAP_val=[]
path_to_events_file_train="/Volumes/xiao_ssd/data/tf_train_v6_20200729_ref04/training/events.out.tfevents.1595976836.3d04c8a9f525"
path_to_events_file_val="/Volumes/xiao_ssd/data/tf_train_v6_20200729_ref04/training/eval_0/events.out.tfevents.1595977727.3d04c8a9f525"
for e in tf.train.summary_iterator(path_to_events_file_train):
    for v in e.summary.value:
        if v.tag=='loss_1':
            steps.append(e.step)
            loss.append(v.simple_value)


for e in tf.train.summary_iterator(path_to_events_file_val):
    for v in e.summary.value:
        if v.tag=='loss':
            steps_val.append(e.step)
            loss_val.append(v.simple_value)
        if v.tag=='PascalBoxes_Precision/mAP@0.5IOU':
            mAP.append(v.simple_value)
# plt.plot(steps,loss)
# plt.plot(steps_val,loss_val)
# plt.xlabel('train_step')
# plt.ylabel('loss')
# plt.legend(['Training','Validation'])
# plt.title('Trainingsvorgang')
# plt.ylim(1,10)
# plt.show()
print(mAP)

