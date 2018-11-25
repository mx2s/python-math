from abc import ABC
from random import randint
import tornado.web

from modules.areas.areas_module import AreasModule
from modules.geometry.degrees_module import DegreesModule
from modules.site.blocks.result_block import ResultBlock
from modules.site.layout_generator import LayoutGenerator


class Geometry1Handler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write(LayoutGenerator.gen_header())

        block = ResultBlock()
        block.title = "Converter from degrees to radian"
        block.table_columns = ["Degrees", "Radians"]

        for i in [1, 15, 120, 180, 360]:
            block.table_data.append([i, DegreesModule.degrees_to_radian(i)])

        for i in range(0, 10):
            num = randint(0, 1000) * 0.25
            block.table_data.append([num, DegreesModule.degrees_to_radian(num)])

        self.write(block.render())

        # ***

        block = ResultBlock()
        block.title = "Converter from degrees to radian"
        block.table_columns = ["Radians", "Degrees"]

        for i in [0.5, 1, 1.5, 4, 10, 1200]:
            block.table_data.append([i, DegreesModule.radian_to_degrees(i)])

        for i in range(1, 10):
            block.table_data.append([i, randint(-1000, 1000) * 0.25])

        self.write(block.render())

        # TODO: finish

        # trapezoid_lists = []
        #
        # for i in range(1, 10):
        #     temp_list = []
        #     for i2 in range(0, 3):
        #         temp_list.append(randint(0, 1000) * 0.25)
        #     trapezoid_lists.append(temp_list)
        #
        # content = "<table border='1' cellpadding='2'>" \
        #           "<tr>" \
        #           "<th>H</th>" \
        #           "<th>B1</th>" \
        #           "<th>B2</th>" \
        #           "<th>Area</th>" \
        #           "</tr>"
        # for data in trapezoid_lists:
        #     content += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>".format(
        #         str(data[0]),
        #         str(data[1]),
        #         str(data[2]),
        #         str(AreasModule.trapezoid_area(data[0], data[1], data[2])))
        # content += "</table>"
        # self.write(content)
        #
        # self.write(LayoutGenerator.gen_title("Cylinder surface area"))
        #
        # cylinders_list = []
        #
        # for i in range(1, 10):
        #     temp_list = []
        #     for i2 in range(0, 2):
        #         temp_list.append(randint(0, 1000) * 0.25)
        #     cylinders_list.append(temp_list)
        #
        # content = "<table border='1' cellpadding='2'>" \
        #           "<tr>" \
        #           "<th>R</th>" \
        #           "<th>H</th>" \
        #           "<th>Total surface area</th>" \
        #           "</tr>"
        #
        # for data in cylinders_list:
        #     content += "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(
        #         str(data[0]),
        #         str(data[1]),
        #         str(AreasModule.cylinder_surface_area(data[0], data[1])))
        # content += "</table>"
        # self.write(content)
        #
        # self.write("</center>")
