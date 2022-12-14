import numpy as np
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import os
import cv2

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('--sample_path', type=str, default='./Guided-Diffusion-Output/sample-no-guided/samples_100x256x256x3.npz')
parser.add_argument('--save_path', type=str, default='./Guided-Diffusion-Output/sample-no-guided/imgs')

def main():
    args = parser.parse_args()
    file = np.load(args.sample_path)
    imgs = file['arr_0']
    labels = file['arr_1']
    num_samples = imgs.shape[0]
    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)
    for i in range(num_samples):
        img = imgs[i,:,:,:]
        label = labels[i]
        cv2.imwrite(os.path.join(args.save_path, f'sample_{i}_class_{label}.jpg'), img)

if __name__ == '__main__':
    main()