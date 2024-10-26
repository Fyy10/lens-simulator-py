import numpy as np


class Color:
    _red = np.uint16([255, 0, 0, 255])
    _green = np.uint16([0, 255, 0, 255])
    _blue = np.uint16([0, 0, 255, 255])
    _white = np.uint16([255, 255, 255, 255])
    _black = np.uint16([0, 0, 0, 255])
    _transparent = np.uint16([0, 0, 0, 0])
    _yellow = np.uint16([255, 255, 0, 255])

    @staticmethod
    def red():
        return Color._red.copy()

    @staticmethod
    def green():
        return Color._green.copy()

    @staticmethod
    def blue():
        return Color._blue.copy()

    @staticmethod
    def white():
        return Color._white.copy()

    @staticmethod
    def black():
        return Color._black.copy()

    @staticmethod
    def transparent():
        return Color._transparent.copy()

    @staticmethod
    def yellow():
        return Color._yellow.copy()

    @staticmethod
    def from_rgba(r: int, g: int, b: int, a: int = 255) -> np.ndarray:
        for val in [r, g, b, a]:
            if not 0 <= val <= 255:
                raise ValueError('RGBA values should be in the range [0, 255], found {}'.format(val))

        return np.uint16([r, g, b, a])

    @staticmethod
    def from_hex(rgb_code: int, a: int=255) -> np.ndarray:
        r = rgb_code >> 16
        g = (rgb_code >> 8) & 0xff
        b = rgb_code & 0xff
        return Color.from_rgba(r, g, b, a)
