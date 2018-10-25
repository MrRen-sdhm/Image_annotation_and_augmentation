# coding:utf8
# 功能：将./images/image*_json文件夹中的label.png和img.png分别提取到./dataset/label和./dataset/img文件夹并重命名

from imutils import paths
import numpy as np
import cv2
import random
import shutil
import os

imagePaths = sorted(list(paths.list_images(path_name)))

for i in range(len(imagePaths)):
    # # 创建文件夹
    # try:
    #     os.makedirs(path_name + str(i))
    # except OSError as e:
    #     if e.errno != 17:
    #         print 'Some issue while creating the directory named -'
    # # 移动|复制文件
    #     #移动
    #     shutil.move(imagePaths[a], path_name + str(i))
    #     #复制
    #     # shutil.copy(imagePaths[a], path_name + str(i))

    basename = os.path.basename(imagePaths[i])
    spliname = os.path.splitext(imagePaths[i])[0]

    # 提取label.png
    if str(basename) == "label.png":
        print imagePaths[i]
        print "basename" + str(i) +":" + basename
        print "spliname" + str(i) +":" + spliname
        parent_path = os.path.dirname(spliname)
        folder_number = parent_path[-6]
        goal_name = "./dataset/label/" + str(folder_number) + ".png"
        print "parent:" + parent_path
        print "number:" + folder_number
        shutil.copy(imagePaths[i], goal_name)
        print "\n"

    # 提取img.png
    if str(basename) == "img.png":
        print imagePaths[i]
        print "basename" + str(i) +":" + basename
        print "spliname" + str(i) +":" + spliname
        parent_path = os.path.dirname(spliname)
        folder_number = parent_path[-6]
        goal_name = "./dataset/img/" + str(folder_number) + ".png"
        print "parent:" + parent_path
        print "number:" + folder_number
        shutil.copy(imagePaths[i], goal_name)
        print "\n"
