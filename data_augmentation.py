# coding:utf8
import cv2
import os
import numpy as np
import imutils
import random

imagePath = "./dataset_test/img/img.jpg"


# 随机操作
def RandOperate(image):
    randnum = random.randint(0, 4)
    if randnum == 0:
        img = SaltNoisy(image)
    elif randnum == 1:
        img = BrightRatio(image)
    elif randnum == 2:
        img = DarkRatio(image)
    elif randnum == 3:
        img = ContrAdj(image)
    elif randnum == 4:
        img = cv2.GaussianBlur(image, (5, 1), 1)
    return img


# 高斯模糊
def Gauss(image):
    return cv2.GaussianBlur(image, (5, 1), 1)


# 椒盐噪声（不适用语意分割）
def SaltNoisy(image):
    img = np.array(image)
    rows, cols, dims = img.shape
    for i in xrange(500):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 255
    return img


# 调亮
def BrightRatio(image):
    bright = random.choice((1.0, 1.1))
    img = np.uint8(np.clip((bright * image + 10), 0, 255))
    return img


# 调暗
def DarkRatio(image):
    bright = random.choice((0.7, 0.8))
    img = np.uint8(np.clip((bright * image + 10), 0, 255))
    return img


# 对比度调整
def ContrAdj(image):
    rows, cols, channels = image.shape
    img = image.copy()
    a = random.choice((0.7, 0.71, 0.72))
    b = 100
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                color = image[i, j][c] * a + b
                if color > 255:
                    img[i, j][c] = 255
                elif color < 0:
                    img[i, j][c] = 0
    return img


# 旋转
def rotate(image):
    angle = random.choice((-15, 15))
    rows, cols, channel = image.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1.0)
    img = cv2.warpAffine(image, M, (cols, rows))

    return img

def rotate(image, label):
    angle = random.choice((-15, 15))
    rows, cols, channel = image.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1.0)
    img = cv2.warpAffine(image.copy(), M, (cols, rows))
    lab = cv2.warpAffine(label.copy(), M, (cols, rows))

    return img, lab


# 拉伸（不适用语意分割）
def stretch(image):
    stretch = random.choice(([1.1, 1], [0.9, 1], [1, 1.1], [1, 0.9], [1, 1]))
    img = cv2.resize(image.copy(), (0, 0), fx=stretch[0], fy=stretch[1],
                     interpolation=cv2.INTER_NEAREST)
    return img


# 平移
def WarpAffine(image):
    rows, cols, channel = image.shape
    # 平移矩阵M：[[1,0,x],[0,1,y]]
    randx = random.choice((-30, -20, -10, 0, 10, 20, 30))
    randy = random.choice((-30, -20, -10, 0, 10, 20, 30))
    M = np.float32([[1,0,randx],[0,1,randy]])
    img = cv2.warpAffine(image, M, (cols,rows))
    return img

def WarpAffine(image, label):
    rows, cols, channel = image.shape
    # 平移矩阵M：[[1,0,x],[0,1,y]]
    randx = random.choice((-30, -20, -10, 0, 10, 20, 30))
    randy = random.choice((-30, -20, -10, 0, 10, 20, 30))
    M = np.float32([[1,0,randx],[0,1,randy]])
    img = cv2.warpAffine(image.copy(), M, (cols,rows))
    lab = cv2.warpAffine(label.copy(), M, (cols,rows))
    # cv2.imshow("image", img)
    # cv2.imshow("lable", lab)
    return img, lab

# 图像和标注增强
def AugImgAndLabel(tmp_img_path, new_img_path, tmp_label_path, new_label_path, img_name, label_name):
    image = cv2.imread(tmp_img_path)
    label = cv2.imread(tmp_label_path)
    # 原始图像
    aug_img_name = os.path.join(new_img_path, "Raw-" + img_name)
    aug_label_name = os.path.join(new_label_path, "Raw-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, image)
    cv2.imwrite(aug_label_name, label)
    # 对比度调整
    aug_img_name = os.path.join(new_img_path, "ContrAdj-" + img_name)
    aug_label_name = os.path.join(new_label_path, "ContrAdj-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, ContrAdj(image.copy()))
    cv2.imwrite(aug_label_name, label)
    # 高斯模糊
    aug_img_name = os.path.join(new_img_path, "Gauss-" + img_name)
    aug_label_name = os.path.join(new_label_path, "Gauss-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, Gauss(image.copy()))
    cv2.imwrite(aug_label_name, label)
    # 左右翻转
    aug_img_name = os.path.join(new_img_path, "flipy-" + img_name)
    aug_label_name = os.path.join(new_label_path, "flipy-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, cv2.flip(image.copy(), 1))
    cv2.imwrite(aug_label_name, cv2.flip(label.copy(), 1))
    # 上下翻转
    aug_img_name = os.path.join(new_img_path, "flipx-" + img_name)
    aug_label_name = os.path.join(new_label_path, "flipx-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, cv2.flip(image.copy(), -1))
    cv2.imwrite(aug_label_name, cv2.flip(label.copy(), -1))
    # 调亮
    aug_img_name = os.path.join(new_img_path, "Bright-" + img_name)
    aug_label_name = os.path.join(new_label_path, "Bright-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, BrightRatio(image.copy()))
    cv2.imwrite(aug_label_name, label)
    # 调暗
    aug_img_name = os.path.join(new_img_path, "Dark-" + img_name)
    aug_label_name = os.path.join(new_label_path, "Dark-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    cv2.imwrite(aug_img_name, DarkRatio(image.copy()))
    cv2.imwrite(aug_label_name, label)
    # 平移
    aug_img_name = os.path.join(new_img_path, "Warp-" + img_name)
    aug_label_name = os.path.join(new_label_path, "Warp-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    img_proc, label_proc = WarpAffine(image.copy(), label.copy())
    cv2.imwrite(aug_img_name, img_proc)
    cv2.imwrite(aug_label_name, label_proc)
    # 旋转
    aug_img_name = os.path.join(new_img_path, "Rotate-" + img_name)
    aug_label_name = os.path.join(new_label_path, "Rotate-" + label_name)
    print "[INFO]aug_img_name:", aug_img_name
    print "[INFO]aug_label_name:", aug_label_name
    img_proc, label_proc = rotate(image.copy(), label.copy())
    cv2.imwrite(aug_img_name, img_proc)
    cv2.imwrite(aug_label_name, label_proc)


def AugDatasetCreate(img_path, new_img_path, label_path, new_label_path):
    #img path
    if os.path.isdir(img_path):
        img_names = os.listdir(img_path)
        img_names.sort() # 排序
    else:
        img_names = [img_path]

    #label path
    if os.path.isdir(label_path):
        label_names = os.listdir(label_path)
        label_names.sort() # 排序
    else:
        label_names = [label_path]

    print "img_names:", img_names
    print "label_names:", label_names

    img_num = 0
    label_num = 0

    #img num
    for img_name in img_names:
        tmp_img_name = os.path.join(img_path, img_name)
        if os.path.isdir(tmp_img_name):
            print('contain file folder')
            exit()
        else:
            img_num = img_num + 1;
    #label num
    for label_name in label_names:
        tmp_label_name = os.path.join(label_path, label_name)
        if os.path.isdir(tmp_label_name):
            print('contain file folder')
            exit()
        else:
            label_num = label_num + 1

    if img_num != label_num:
        print('the num of img and label is not equl')
        exit()
    else:
        num = img_num

    for i in range(num):
        img_name = img_names[i]
        print "[INFO]img_name:", img_name
        label_name = label_names[i]
        print "[INFO]label_name:", label_name

        tmp_img_name = os.path.join(img_path, img_name)
        print "[INFO]tmp_img_name:", tmp_img_name
        tmp_label_name = os.path.join(label_path, label_name)
        print "[INFO]tmp_label_name:", tmp_label_name

        # 图像和标注增强
        AugImgAndLabel(tmp_img_name, new_img_path, tmp_label_name, new_label_path, img_name, label_name);



def main():
    # image = cv2.imread(imagePath)
    # cv2.imshow("image", image)

    # # # 修改对比度
    # Contr = ContrAdj(image)
    # cv2.imshow("ContrAdj", Contr)
    # # 拉伸变换
    # # Stretch = stretch(image)
    # # cv2.imshow("Stretch", Stretch)
    # # 添加椒盐噪声
    # # Noisy = SaltNoisy(image.copy())
    # # cv2.imshow("SaltNoisy", Noisy)
    # # 高斯模糊 (25,25,5)>(15,15,5)>(5,5,5)>(5,1,1)>(1,1,5)
    # gauss = Gauss(image.copy())
    # cv2.imshow("Gauss", gauss)
    # # 左右反转
    # flip1 = cv2.flip(image.copy(), 1)
    # cv2.imshow("flip1", flip1)
    # # 上下反转
    # flip_1 = cv2.flip(image.copy(), -1)
    # cv2.imshow("flip_1", flip_1)
    # # 调亮
    # Bright = BrightRatio(image)
    # cv2.imshow("Bright", Bright)
    # # 调暗
    # Dark = DarkRatio(image)
    # cv2.imshow("Dark", Dark)
    # # 旋转
    # rot = rotate(image)
    # cv2.imshow("Rotate", rot)
    # # 平移
    # warp = WarpAffine(image)
    # cv2.imshow("warpAffine", warp)
    # # 随机操作
    # # image = RandOperate(image)
    # # cv2.imshow("RandOperate", image)

    # cv2.waitKey(0)

    AugDatasetCreate("./dataset_test/img",
              "./dataset_aug_test/img",
              "./dataset_test/label",
              "./dataset_aug_test/label")


if __name__ == "__main__":
    main()
