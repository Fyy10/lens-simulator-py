import matplotlib.pyplot as plt

from camera import *
from utils import *


def main(filename: str):
    lens = Lens(f=Config.focal_length, r=Config.focal_ratio, v=Config.sensor_dist)
    camera = Camera(
        lens,
        origin=np.array([.0, -100.0, .0]),
        pointing_dir=np.array([.0, 1.0, .0]),
        up_dir=np.array([.0, .0, 1.0]),
        sensor_xlim=Config.sensor_xlim
    )

    Scene.init()

    img = camera.get_image()

    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()

    # img.show()
    img.save('img/' + filename)


if __name__ == '__main__':
    # f
    focal_length = [40.0, 50.0, 60.0]  # f/2.0, focus 100mm
    # aperture
    fnums = [4.0, 8.0, 32.0, 64.0]  # 50mm, focus 100mm
    # u
    focal_dist = [90.0, 100.0, 110.0, 150.0, 200.0]  # 50mm, f/1.8

    # f/2.0, focus at 100mm
    Config.focal_ratio = 2.0
    for f in focal_length:
        Config.focal_length = f
        Config.sensor_dist = 100.0 * f / (100.0 - f)
        filename = '{}mm_f{}_{}.png'.format(int(Config.focal_length), int(Config.focal_ratio), int(100.0))
        print(filename)
        main(filename)

    # 50mm, focus at 100mm
    Config.focal_length = 50.0
    Config.sensor_dist = 100.0
    for r in fnums:
        Config.focal_ratio = r
        filename = '{}mm_f{}_{}.png'.format(int(Config.focal_length), int(Config.focal_ratio), int(100.0))
        print(filename)
        main(filename)

    # 50mm f/1.8
    Config.focal_length = 50.0
    Config.focal_ratio = 1.8
    for u in focal_dist:
        Config.sensor_dist = u * Config.focal_length / (u - Config.focal_length)
        filename = '{}mm_f{}_{}.png'.format(int(Config.focal_length), Config.focal_ratio, int(u))
        print(filename)
        main(filename)

    # exp dof
    # baseline: 50mm f/2 100mm
    # 25mm f/1 100mm (same aperture as baseline)
    Config.focal_length = 25.0
    Config.focal_ratio = 1.0
    Config.sensor_dist = 100.0 * Config.focal_length / (100.0 - Config.focal_length)
    Config.sensor_xlim = Config.sensor_dist  # same angle of view as baseline
    main('exp_dof/25mm_f1_100.png')

    # 25mm f/2 100mm
    Config.focal_ratio = 2.0
    main('exp_dof/25mm_f2_100.png')
