import math


class AreasModule:
    @staticmethod
    def trapezoid_area(h: float, b1: float, b2: float):
        return ((b1 + b2) / 2) * h

    @staticmethod
    def cylinder_surface_area(r: float, h: float):
        return (2 * math.pi * r * h) + (2 * math.pi * (r * r))

    @staticmethod
    def sphere_surface_area(r: float, h: float):
        return (4 * math.pi * r * h) + (2 * math.pi * (r * r))
