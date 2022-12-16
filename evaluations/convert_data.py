import numpy as np
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import os
import cv2

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('--img_path', type=str, default='./datasets/CottonWeedID15-sub-sample100')
parser.add_argument('--save_path', type=str, default='./datasets/data-100.npz')

def main():
    args = parser.parse_args()
    imgs = []
    for img_name in os.listdir(args.img_path):
        img = cv2.imread(os.path.join(args.img_path, img_name))
        img = cv2.resize(img,(256,256))
        imgs.append(img)
    imgs = np.array(imgs)
    out_path = os.path.join(args.save_path)
    np.savez(out_path, imgs)
    
        

if __name__ == '__main__':
    main()