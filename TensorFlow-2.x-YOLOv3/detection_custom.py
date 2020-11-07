#================================================================
#
#   File name   : detection_demo.py
#   Author      : PyLessons
#   Created date: 2020-05-18
#   Website     : https://pylessons.com/
#   GitHub      : https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3
#   Description : object detection image and video example
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.yolov3 import Create_Yolov3
from yolov3.utils import load_yolo_weights, detect_image, detect_video, detect_realtime
from yolov3.configs import *
import time

if tf.test.gpu_device_name(): 

    print('-------->>Default GPU Device:{}'.format(tf.test.gpu_device_name()))

else:

   print("Please install GPU version of TF")
input_size = YOLO_INPUT_SIZE
Darknet_weights = YOLO_DARKNET_WEIGHTS
# if TRAIN_YOLO_TINY:
#     Darknet_weights = YOLO_DARKNET_TINY_WEIGHTS
time_s = time.time()
video_path = ["Test_Video/people_walking_3.mp4"]
# image_path = ["test_images_and_videos/deer_cow.jpg",
# 			"test_images_and_videos/84353914_188324fbb9_b.jpg",
# 			"test_images_and_videos/87180235_d8bb660c55_b.jpg",
# 			"test_images_and_videos/91693053_6c39a7192c_o.jpg",
# 			"test_images_and_videos/manymanydeers.jpg"] 
yolo = Create_Yolov3(input_size=input_size, CLASSES=TRAIN_CLASSES)
yolo.load_weights("./checkpoints/yolov3_custom") # use keras weights
count=0
# for i in image_path:
# 	detect_image(yolo, i, "./IMAGES/new_image_"+str(count)+".jpg", input_size=input_size, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
# 	count+=1
for v in video_path:
	detect_video(yolo, v, "./IMAGES/Result_CCTV_Video"+str(count)+".mp4", input_size=input_size, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
	count+=1
time_end = time.time()
time_total = time_end - time_s
print('Total Time YOLO V3: > ', time_total)
#detect_realtime(yolo, '', input_size=input_size, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))
