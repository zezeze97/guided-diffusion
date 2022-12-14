import os
import random
import shutil

src_path = './datasets/CottonWeedID15-sub10'
target_path = './datasets/CottonWeedID15-sub-sample100'
sample_num = 100

img_name_lst = os.listdir(src_path)
img_name_lst = random.sample(img_name_lst, sample_num)
for img_name in img_name_lst:
    src = os.path.join(src_path,img_name)
    target = os.path.join(target_path, img_name)
    shutil.copy(src, target)