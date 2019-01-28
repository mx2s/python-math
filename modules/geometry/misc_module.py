import math


class MiscModule:
    @staticmethod
    def get_arc_length(a: float, r: float):
        while a > 360:
            a -= 360
        return (a / 360) * (2 * math.pi) * r

    @staticmethod
    def get_sector_area(a: float, r: float):
        while a > 360:
            a -= 360
        return math.pi * (r * r) * (a / 360)

    @staticmethod
    def get_discriminant(a: float, b: float, c: float):
        return (b * b) - (4 * a * c)
