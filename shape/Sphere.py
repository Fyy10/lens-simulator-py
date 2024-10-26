from typing import Tuple
import numpy as np

from material import Material
from utils import Ray
from shape.Shape import Shape


class Sphere(Shape):
    def __init__(self, origin: np.ndarray, r: float, material: Material):
        super().__init__(material)
        # (x-x0)^2 + (y-y0)^2 + (z-z0)^2 = r^2
        self.origin = origin  # [x0, y0, z0]
        self.r = r

    def hit(self, ray: Ray) -> Tuple[float, np.ndarray]:
        # ray function: origin + t * direction
        # solve for at^2 + bt + c = 0
        # a = ray.direction_x^2 + ray.direction_y^2 + ray.direction_z^2
        ray.normalize()
        a = 1.0
        # b = 2 (ray.direction dot (ray.origin - self.origin))
        b = 2 * ray.direction.dot(ray.origin - self.origin)
        # c = squared_sum(ray.origin - self.origin) - self.r^2
        c = np.square(ray.origin - self.origin).sum() - self.r ** 2

        # b^2 - 4ac
        delta = b ** 2 - 4 * a * c
        if self.float_leq(delta, 0.0):
            # delta <= 0, no hit
            return self.no_hit_ret()
        else:
            delta = np.sqrt(delta)
            # roots: -b +- delta / 2*a
            t1 = (-b + delta) / 2.0
            t2 = (-b - delta) / 2.0

            # only count for t > 0
            pos = []
            if not self.float_leq(t1, 0.0):
                pos.append(t1)
            if not self.float_leq(t2, 0.0):
                pos.append(t2)

            if len(pos) == 2:
                t = min(pos)
                p = ray.at(t)
                n = (p - self.origin) / self.r
                assert self.float_leq(ray.direction.dot(n), 0.0)
                return t, n
            else:
                # if count(t > 0) <= 1, then there is no hit on surface
                return self.no_hit_ret()
