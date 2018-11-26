from abc import ABC
from random import randint
import tornado.web

from modules.geometry.volumes_module import VolumesModule
from modules.geometry.areas_module import AreasModule
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

        # ***

        block = ResultBlock()
        block.title = "Trapezoid area"
        block.table_columns = ["H", "B1", "B2", "Area"]

        for i in range(1, 10):
            temp_list = []
            for i2 in range(0, 4):
                temp_list.append(randint(0, 1000) * 0.25)
            temp_list[3] = AreasModule.trapezoid_area(temp_list[0], temp_list[1], temp_list[2])

            block.table_data.append(temp_list)

        self.write(block.render())

        # ***

        block = ResultBlock()
        block.title = "Cylinder total surface area and volume"
        block.table_columns = ["R", "H", "Total surface area", "Volume"]

        for i in range(1, 10):
            temp_list = []
            for i2 in range(0, 4):
                temp_list.append(randint(0, 400) * 0.25)
            temp_list[2] = AreasModule.cylinder_surface_area(temp_list[0], temp_list[1])
            temp_list[3] = VolumesModule.cylinder_volume(temp_list[0], temp_list[1])

            block.table_data.append(temp_list)

        self.write(block.render())

        # ***

        block = ResultBlock()
        block.title = "Sphere total surface area and volume"
        block.table_columns = ["R", "H", "Surface area", "Volume"]

        for i in range(1, 10):
            temp_list = []
            for i2 in range(0, 4):
                temp_list.append(randint(0, 400) * 0.25)
            temp_list[2] = AreasModule.cylinder_surface_area(temp_list[0], temp_list[1])
            temp_list[3] = VolumesModule.cylinder_volume(temp_list[0], temp_list[1])

            block.table_data.append(temp_list)

        self.write(block.render())
