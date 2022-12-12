import os
import shutil

base_path = "datasets/CottonWeedID15"
target_base_path = "/mnt/disk1/zhangzr/dataset/CottonWeedID-sub10"
class_list = os.listdir(base_path)

for class_name in class_list:
    class_path = os.path.join(base_path, class_name)
    for i,image_name in enumerate(os.listdir(class_path)):
        src_path = os.path.join(class_path, image_name)
        target_path = os.path.join(target_base_path, f"{class_name}_{i}.jpg")
        shutil.copy(src_path, target_path)
        
        
