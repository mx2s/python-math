from abc import ABC
import tornado.web

from modules.geometry.degrees_module import DegreesModule
from modules.site.layout_generator import LayoutGenerator


class Geometry1Handler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write(LayoutGenerator.gen_header())
        self.write(LayoutGenerator.gen_title("Converter from degrees to radian"))

        degrees_to_check = [1, 15, 20, 40, 60, 80, 90, 120, 180, 360]

        content = "<ul>"
        for degrees in degrees_to_check:
            content += "<li>{0} degrees to radians: {1}</li>".format(str(degrees),
                                                                     str(DegreesModule.degrees_to_radian(degrees)))
        content += "</ul>"
        self.write(content)
