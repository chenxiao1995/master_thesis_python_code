#!/usr/bin/env python3

import tensorflow.lite as lite
import time
import numpy as np
import PIL
import detect
from PIL import Image,ImageDraw

# from coco import image_classes

ms = lambda: int(round(time.time() * 1000))

model_path = "/Users/xiao/inference_edge_tpu/ssd_mobilenet.tflite"

is_quant = "quant" in model_path.lower()
print(is_quant)

def get_mobilenet_input(f, out_size=(300, 300), is_quant=True):
    img = np.array(PIL.Image.open(f).resize(out_size))
    print(img.shape)
    if not (is_quant):
        img = img.astype(np.float32) / 128 - 1
    return np.array([img])


def print_coco_label(cl_id, t):
    print("class: {}, label: {}, time: {:,} ms".format(cl_id, image_classes[cl_id], t))


def print_output(inp_files, res):
    boxes, classes, scores, num_det = res

    for i, fname in enumerate(inp_files):
        n_obj = int(num_det[i])

        print("{} - found objects:".format(fname))
        for j in range(n_obj):
            cl_id = int(classes[i][j]) + 1
            label = cl_id
            score = scores[i][j]
            if score < 0.5:
                continue
            box = boxes[i][j]
            print("  ", cl_id, label, score, box)


ip = lite.Interpreter(model_path=model_path)
ip.allocate_tensors()
image=Image.open('/Users/xiao/inference_edge_tpu/a1_4.png')
scale = detect.set_input(ip, image.size,
                       lambda size: image.resize(size, Image.ANTIALIAS))
# inp_id = ip.get_input_details()[0]["index"]
# out_det = ip.get_output_details()
# out_id0 = out_det[0]["index"]
# out_id1 = out_det[1]["index"]
# out_id2 = out_det[2]["index"]
# out_id3 = out_det[3]["index"]

# img = get_mobilenet_input('/Users/xiao/inference_edge_tpu/a1_4.png', is_quant=is_quant)
# print(img.shape)
# ip.set_tensor(inp_id, img)
# ip.invoke()
# boxes = ip.get_tensor(out_id0)
# classes = ip.get_tensor(out_id1)
# scores = ip.get_tensor(out_id2)
# num_det = ip.get_tensor(out_id3)
#
#
#
# print(boxes)
# print(classes)
# print(scores)

# objs = detect.get_output(ip, 0, scale)
# print(objs)
inp_id = ip.get_input_details()[0]["index"]
out_det = ip.get_output_details()
out_id0 = out_det[0]["index"]
out_id1 = out_det[1]["index"]
out_id2 = out_det[2]["index"]
out_id3 = out_det[3]["index"]

images = ['/Users/xiao/inference_edge_tpu/a1_4.png']


for f in images:
    img = get_mobilenet_input(f, is_quant=is_quant)
    print(img.shape)
    ip.set_tensor(inp_id, img)
    ip.invoke()
    boxes = ip.get_tensor(out_id0)
    classes = ip.get_tensor(out_id1)
    scores = ip.get_tensor(out_id2)
    num_det = ip.get_tensor(out_id3)
    # print([boxes, classes, scores, num_det])
    # print_output([f], [boxes, classes, scores, num_det])