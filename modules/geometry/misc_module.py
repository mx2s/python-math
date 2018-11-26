import math


class MiscModule:
    @staticmethod
    def get_arc_length(a: float, r: float):
        return (a / 360) * (2 * math.pi) * r
