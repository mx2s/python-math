from abc import ABC
from random import randint
import tornado.web

from modules.geometry.misc_module import MiscModule
from modules.site.blocks.result_block import ResultBlock
from modules.site.layout_generator import LayoutGenerator


class Geometry2Handler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write(str(MiscModule.get_arc_length(90,4)))
        self.write(LayoutGenerator.gen_header())

        block = ResultBlock()
        block.title = "Arc length of an angle"
        block.table_columns = ["Angle", "Radius", "Result"]

        for i in range(0, 10):
            arr = [
                randint(0, 10000) * 0.5,
                randint(0, 10000) * 0.5
            ]
            arr.append(MiscModule.get_arc_length(arr[0], arr[1]))
            block.table_data.append(arr)

        self.write(block.render())
