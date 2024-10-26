from typing import Tuple
import numpy as np

from material import PureColor
from utils import Ray, Color, Config
from shape import *


class Scene:
    objects = []

    @staticmethod
    def init():
        # sphere at (0, 0, 0), r = 15, color red
        Scene.objects.append(
            Sphere(
                np.array([0.0, 0.0, 0.0]), 15.0,
                material=PureColor(Color.red())
            )
        )
        # sphere at (-15, -15, 0), r = 15, color green
        Scene.objects.append(
            Sphere(
                np.array([-15.0, -15.0, 0.0]), 15.0,
                material=PureColor(Color.green())
            )
        )
        # sphere at (15, 15, 0), r = 15, color blue
        Scene.objects.append(
            Sphere(
                np.array([15.0, 15.0, 0.0]), 15.0,
                material=PureColor(Color.blue())
            )
        )
        # plane at z = -50, pointing z+
        Scene.objects.append(
            Plane(
                Ray(np.array([0.0, 0.0, -50.0]), np.array([0.0, 0.0, 1.0])),
                material=PureColor(Color.from_hex(0xcce5ff))  # sky blue
            )
        )
        # plane at z = 50, pointing z-
        Scene.objects.append(
            Plane(
                Ray(np.array([0.0, 0.0, 50.0]), np.array([0.0, 0.0, -1.0])),
                material=PureColor(Color.from_hex(0xccffcc))  # light green
            )
        )
        # plane at y = 100, pointing y-
        Scene.objects.append(
            Plane(
                Ray(np.array([0.0, 100.0, 0.0]), np.array([0.0, -1.0, 0.0])),
                material=PureColor(Color.from_hex(0xffffcc))  # light yellow
            )
        )
        # plane at x = -50, pointing x+
        Scene.objects.append(
            Plane(
                Ray(np.array([-50.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0])),
                material=PureColor(Color.from_hex(0xffcce5))  # pink
            )
        )
        # plane at x = 50, pointing x-
        Scene.objects.append(
            Plane(
                Ray(np.array([50.0, 0.0, 0.0]), np.array([-1.0, 0.0, 0.0])),
                material=PureColor(Color.from_hex(0xe5ccff))  # light purple
            )
        )

    @staticmethod
    def hit(ray: Ray) -> Tuple:
        # ray function: origin + t * direction
        # return the hit object index, param t in ray func, and the surface normal vector of the hit object
        # ray dot normal is guaranteed to be negative
        # if no hit, return -1, 0.0, zero vec

        intersections = []  # list of (i, t, n)
        for i, obj in enumerate(Scene.objects):
            t, n = obj.hit(ray)
            if t > 0.0:
                intersections.append((i, t, n))

        if intersections:
            # sort by t inc
            intersections.sort(key=lambda x: x[1])
            return intersections[0]
        else:
            return -1, 0.0, np.zeros(3, dtype=float)

    @staticmethod
    def ray_color(ray: Ray, depth: int = Config.max_reflection_depth) -> np.ndarray:
        if depth <= 0:
            # reaches depth limit, no light (dark)
            return Color.black()

        i, t, n = Scene.hit(ray)
        if i < 0:
            # no hit, return background color
            return Color.white()

        return Scene.objects[i].ray_color(ray, depth - 1)
