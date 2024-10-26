import numpy as np

from utils import Ray, Color


class Material:
    """
    Base class of material
    """
    def ray_color(self, ray: Ray, depth: int) -> np.ndarray:
        raise NotImplementedError()
