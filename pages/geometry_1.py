from abc import ABC
import tornado.web

from modules.geometry.degrees_module import DegreesModule
from modules.site.layout_generator import LayoutGenerator


class Geometry1Handler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write(LayoutGenerator.gen_header())
        self.write(LayoutGenerator.gen_title("Converter from degrees to radian"))

        degrees_to_check = [1, 15, 20, 40, 60, 80, 90, 120, 180, 360]

        self.write("<center>")
        content = "<table border='1' cellpadding='2'>" \
                  "<tr>" \
                  "<th>Degrees</th>" \
                  "<th>Radians</th>" \
                  "</tr>"
        for degrees in degrees_to_check:
            content += "<tr><td>{0}</td><td>{1}</td></tr>".format(str(degrees),
                                                                  str(DegreesModule.degrees_to_radian(degrees)))
        content += "</table>"
        self.write(content)

        self.write(LayoutGenerator.gen_title("Converter from radian to degrees"))

        radians_list = [0, 0.5, 1, 1.5, 2, 4, 6, 8, 10, 1200, -5]

        content = "<table border='1' cellpadding='2'>" \
                  "<tr>" \
                  "<th>Radians</th>" \
                  "<th>Degrees</th>" \
                  "</tr>"
        for radians in radians_list:
            content += "<tr><td>{0}</td><td>{1}</td></tr>".format(str(radians),
                                                                      str(DegreesModule.radian_to_degrees(radians)))
        content += "</table>"
        self.write(content)
        self.write("</center>")
