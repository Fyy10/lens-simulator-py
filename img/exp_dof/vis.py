from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread

def fname_decode(fname: str) -> Tuple[int, float]:
    fname = fname.split('/')[-1]
    fname = fname.split('.')[0]
    fname = fname.split('_')
    return int(fname[0][:-2]), float(fname[1][1:])

def main():
    fnames = ['../50mm_f2_100.png', '25mm_f1_100.png', '25mm_f2_100.png']

    fig, axes = plt.subplots(1, len(fnames), figsize=(15, 5))
    for i, fname in enumerate(fnames):
        img = imread(fname)
        axes[i].imshow(img)
        axes[i].axis('off')
        axes[i].set_title('{}mm f/{} focused at 100mm'.format(*fname_decode(fname)))
    plt.tight_layout()
    plt.savefig('exp_dof.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
