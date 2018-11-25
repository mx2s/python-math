import math


class DegreesModule:
    @staticmethod
    def degrees_to_radian(degrees: float):
        return (degrees * math.pi) / 180

    @staticmethod
    def radian_to_degrees(radian: float):
        return radian * (180 / math.pi)
