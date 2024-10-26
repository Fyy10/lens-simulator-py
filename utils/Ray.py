import numpy as np


class Ray:
    def __init__(self, origin: np.ndarray, direction: np.ndarray):
        # Ray function: origin + t * direction
        self.origin = origin
        self.direction = direction

        # rgba
        self.color = np.array([.0, .0, .0, .0])

        self.normalize()

    def length(self) -> float:
        return np.linalg.norm(self.direction).item()

    # convert to unit vector
    def normalize(self):
        self.direction /= self.length()

    # returns a 3D point
    def at(self, t: float) -> np.ndarray:
        return self.origin + t * self.direction
