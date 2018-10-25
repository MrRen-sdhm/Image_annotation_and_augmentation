import cv2
import os
import numpy as np
import imutils
import shutil
from imutils import paths

# imagePath_in = "./img"
# imagePath_out = "./img_resize/"
imagePath_in = "./label"
imagePath_out = "./label_resize/"


print "[Info] clean folder imagePath_out"
shutil.rmtree(imagePath_out)
os.mkdir(imagePath_out)

imagePaths = sorted(list(paths.list_images(imagePath_in)))

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (256, 256))
    # image = cv2.resize(image, (0, 0), fx=0.1, fy=0.1,
    #                    interpolation=cv2.INTER_NEAREST)

    basename = os.path.basename(imagePath)
    print '[Info] resize:', basename
    cv2.imwrite(imagePath_out + basename, image)
