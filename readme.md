### 1、将所有待标注图像放到./images文件夹，命名为image\*.jpg，使用labelme标注，并将标注文件\*.json保存到./images文件夹
### 2、根据图片张数修改labelme_all.sh中的image_num，再运行指令bash labelme_all.sh，根据所有\*.json文件，在./images文件夹下生成包含原始图像和标注图像的image*_json文件夹
### 3、运行指令python label_collect.py，将./images/image*_json文件夹中的label.png和img.png分别提取到./dataset/label和./dataset/img文件夹并重命名
### 4、使用python convert2binary.py将标注所得带有颜色的标注图片转换为二值图
### 5、使用python data_augmentation.py进行语意分割数据集中图片的增强，同时生成增强后图像的标注