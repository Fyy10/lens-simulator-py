from typing import Tuple
import numpy as np

from material import Material
from utils import Ray


class Shape:
    """
    Base class of shape
    """
    eps = 1e-8

    def __init__(self, material: Material):
        self.material = material

    def hit(self, ray: Ray) -> Tuple[float, np.ndarray]:
        """
        Ray function: origin + t * direction.
        Return the ray param t and surface normal vector if the ray hits the object.
        Return -1.0, zero vec if it does not hit.
        """
        raise NotImplementedError()

    def no_hit_ret(self) -> Tuple[float, np.ndarray]:
        return -1.0, np.zeros(3, dtype=float)

    def float_leq(self, v1: float, v2: float) -> bool:
        """
        Return True if v1 <= v2, otherwise return False
        """
        v1 -= v2
        return v1 < 0.0 or abs(v1) < self.eps

    def ray_color(self, ray: Ray, depth: int) -> np.ndarray:
        return self.material.ray_color(ray, depth)
