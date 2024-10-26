from typing import Tuple
import numpy as np

from material import Material
from utils import Ray
from shape.Shape import Shape


class Plane(Shape):
    def __init__(self, surface_normal_ray: Ray, material: Material):
        super().__init__(material)
        # Ax + By + Cz + D = 0
        surface_normal_ray.normalize()
        # [A, B, C]
        self.normal = surface_normal_ray.direction
        # D
        self.D = -self.normal.dot(surface_normal_ray.origin)

    def hit(self, ray: Ray) -> Tuple[float, np.ndarray]:
        dot_prod = ray.direction.dot(self.normal)
        if self.float_leq(0.0, dot_prod):
            # ray.dir dot normal >= 0, no hit
            return self.no_hit_ret()

        # self.normal dot [x, y, z].T + D = 0
        # [x, y, z].T = ray.at(t)
        # solve for t
        # normal dot origin + t * normal dot direction + D = 0
        t = (-self.D - self.normal.dot(ray.origin)) / dot_prod

        if self.float_leq(t, 0.0):
            # t <= 0, no hit
            return self.no_hit_ret()
        else:
            return t, self.normal
