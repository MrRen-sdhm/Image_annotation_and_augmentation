# coding:utf8
# 此脚本将得到的标注后得到的有色标注图像转换为黑白图像
import cv2
import os
import numpy as np
import shutil
import imutils
import random
from imutils import paths

# imagePath = "./images/image1.jpg"
# imagePath = "./images/image1_json/label.png"

imagePath_in = "./dataset_aug_test/label_resize/"
imagePath_out = "./dataset_aug_test/label_process/"


print "[Info] clean folder imagePath_out"
shutil.rmtree(imagePath_out)
os.mkdir(imagePath_out)

imagePaths = sorted(list(paths.list_images(imagePath_in)))

for imagePath in imagePaths:
    image = cv2.imread(imagePath)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 0, 255,
                           cv2.THRESH_BINARY)[1]

    basename = os.path.basename(imagePath)
    print '[Info] Process:', basename
    cv2.imwrite(imagePath_out + basename, image)

    # cv2.imshow('img', image)

    # key = cv2.waitKey(0)


