import numpy as np

from material import Material
from utils import Ray, Color


class PureColor(Material):
    def __init__(self, color: np.ndarray):
        self.color = color

    def ray_color(self, ray: Ray, depth: int) -> np.ndarray:
        return self.color.copy()
