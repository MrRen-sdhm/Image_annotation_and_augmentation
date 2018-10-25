#!/bin/bash
s1="./images/image"
s2=".json"
image_num=3 # modify the number of images here
for((i=1;i<image_num+1;i++))
do
s3=${i}
labelme_json_to_dataset ${s1}${s3}${s2}
done
