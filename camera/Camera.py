import numpy as np
from PIL import Image
from tqdm import trange

from camera import Lens
from utils import Color, Scene, Config
from utils import Ray


class Camera:
    """
    Defines a camera

    :param lens: Lens
    :param origin: the origin of the camera, which is also the origin of the camera lens
    :param pointing_dir: the direction that the camera points to
    :param up_dir: the up direction of the camera
    :param sensor_xlim: sensor size in the x direction
    :param aspect_ratio: sensor_zlim / sensor_xlim
    :param resolution_x: resolution of sensor in the x-axis
    """

    def __init__(
            self, lens: Lens,
            origin: np.ndarray, pointing_dir: np.ndarray, up_dir: np.ndarray,
            sensor_xlim: float = 100.0, aspect_ratio: float = 4 / 3,
            resolution_x: int = 800
    ):
        self.lens = lens
        self.origin = origin
        self.pointing_dir = pointing_dir
        self.up_dir = up_dir
        self.sensor_xlim = sensor_xlim
        self.aspect_ratio = aspect_ratio
        self.sensor_zlim = sensor_xlim / self.aspect_ratio
        self.res_x = resolution_x
        self.res_z = int(resolution_x / self.aspect_ratio)

    def get_image(self) -> Image.Image:
        # image height: self.res_z
        # image width: self.res_x

        # (res_z,) (H,)
        sensor_z = np.linspace(-.5 * self.sensor_zlim, .5 * self.sensor_zlim, self.res_z)
        image_z = self.lens.get_image_pixels(sensor_z)
        # (res_x,) (W,)
        sensor_x = np.linspace(-.5 * self.sensor_xlim, .5 * self.sensor_xlim, self.res_x)
        image_x = self.lens.get_image_pixels(sensor_x)

        # (H, W, C), C = 4 for RGBA img
        img_data = np.zeros((self.res_z, self.res_x, 4), dtype=np.uint8)

        # TODO: try parallel
        for i in trange(self.res_z):
            for j in range(self.res_x):
                # TODO: use the correct coordinate for cameras in any position and direction
                # current implementation only works for cameras pointing y+ and up dir is z+
                ux = image_x[j]
                uy = self.lens.u
                uz = image_z[i]

                tgt = self.origin + np.array([ux, uy, uz], dtype=float)
                # (aperture_sample_size, 3)
                src_l = self.lens.aperture_samples() + self.origin

                pixel_color = Color.transparent()
                for src in src_l:
                    ray = Ray(src, tgt - src)
                    pixel_color += Scene.ray_color(ray)
                pixel_color //= len(src_l)

                img_data[self.res_z - i - 1, j] = pixel_color

        # rgba image: (H, W, 4)
        # R: 0-255
        # G: 0-255
        # B: 0-255
        # A: 0-255
        img = Image.fromarray(np.uint8(img_data))
        return img
