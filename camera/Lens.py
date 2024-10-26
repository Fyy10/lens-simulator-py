import numpy as np
from utils import Config


class Lens:
    """
    Defines a lens

    :param f: focal length
    :param r: focal ratio, e.g., r=1.8 for f/1.8 aperture, also known as f-number
    :param v: distance between the image sensor and the lens
    """

    def __init__(self, f: float, r: float, v: float):
        # focal length
        self.f = f
        # focal ratio
        self.r = r

        # distance between the image sensor and the lens
        self.v = 0.0
        # distance between the lens and the focal plane
        self.u = 0.0
        self.set_v(v)

    def set_f(self, f):
        if f > self.v:
            raise ValueError('f={}mm cannot be greater than v={}mm'.format(f, self.v))
        self.f = f
        self.update_u()

    def set_v(self, v):
        if v < self.f:
            raise ValueError('v={}mm cannot be less than f={}mm'.format(v, self.f))
        self.v = v
        self.update_u()

    def update_u(self):
        if self.v < self.f:
            raise ValueError('v={}mm cannot be less than f={}mm'.format(self.v, self.f))
        # 1/u + 1/v = 1/f
        # u = vf/(v-f)
        self.u = self.v * self.f / (self.v - self.f)

    def get_image_pixels(self, sensor_pixels: np.ndarray) -> np.ndarray:
        """
        Compute the coordinates (ux, uz) on the focal plane given the image sensor pixels (vx, vz)

        :param sensor_pixels: ndarray of shape (N,) where sensor_pixels[i] gives vx or vz

        :return: ndarray of shape (N,)
        """
        return sensor_pixels * self.u / self.v

    def aperture_samples(self, sample_size: int = Config.aperture_sample_size) -> np.ndarray:
        """
        Uniformly sample points on the aperture

        :param sample_size: number of sample points
        :return: ndarray of shape (n, 3) while y = 0
        """
        radius = self.f / self.r
        radius /= 2

        theta = np.random.uniform(0, 2 * np.pi, sample_size)
        ro = radius * np.sqrt(np.random.uniform(0, 1, sample_size))

        # (sample_size,)
        x = ro * np.cos(theta)
        y = np.zeros(sample_size, dtype=float)
        z = ro * np.sin(theta)

        # returns (sample_size, 3)
        return np.vstack([x, y, z], dtype=float).T
