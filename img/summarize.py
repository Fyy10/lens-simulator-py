import os
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread


def fname_decode(filename: str) -> Tuple[int, float, int]:
    filename = '.'.join(filename.split('.')[:-1])
    l = filename.split('_')
    f = int(l[0][:-2])
    r = float(l[1][1:])
    u = int(l[2])
    return f, r, u


def fname_encode(f: int, r: float, u: int) -> str:
    if abs(r - int(r)) < 1e-8:
        r = int(r)
    return '{}mm_f{}_{}.png'.format(f, r, u)


def main():
    fs = []
    rs = []
    us = []
    for filename in os.listdir():
        if filename.split('.')[-1].lower() != 'png':
            continue
        # print(fname_encode(*fname_decode(filename)))
        f, r, u = fname_decode(filename)
        for l, v in zip([fs, rs, us], [f, r, u]):
            if v in l:
                continue
            l.append(v)

    # f/2.0, u 100mm
    r = 2.0
    u = 100
    fig, axes = plt.subplots(1, len(fs), figsize=(15, 5))
    for i, f in enumerate(sorted(fs)):
        img = imread(fname_encode(f, r, u))
        axes[i].imshow(img)
        axes[i].axis('off')
        axes[i].set_title('{}mm f/{} focused at {}mm'.format(f, r, u))
    plt.tight_layout()
    # plt.show()
    plt.savefig('combined/f2_100.png', bbox_inches='tight')

    # f 50mm, u 100mm
    f = 50
    u = 100
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    for i, r in enumerate(sorted(rs)):
        img = imread(fname_encode(f, r, u))
        axes[i].imshow(img)
        axes[i].axis('off')
        axes[i].set_title('{}mm f/{} focused at {}mm'.format(f, r, u))
    for i in range(len(rs), len(axes)):
        axes[i].imshow(np.zeros((600, 800, 4)))  # placeholder
        axes[i].axis('off')
    plt.tight_layout()
    # plt.show()
    plt.savefig('combined/50mm_100.png', bbox_inches='tight')

    # f 50mm, f/1.8
    f = 50
    r = 1.8
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    for i, u in enumerate(sorted(us)):
        img = imread(fname_encode(f, r, u))
        axes[i].imshow(img)
        axes[i].axis('off')
        axes[i].set_title('{}mm f/{} focused at {}mm'.format(f, r, u))
    for i in range(len(us), len(axes)):
        axes[i].imshow(np.zeros((600, 800, 4)))  # placeholder
        axes[i].axis('off')
    plt.tight_layout()
    # plt.show()
    plt.savefig('combined/50mm_f1.8.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
