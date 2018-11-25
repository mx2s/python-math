from abc import ABC
import tornado.web

from modules.site.layout_generator import LayoutGenerator


class IndexHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        categories_list = [
            {"name": "Geometry 1", "uri": "/geometry_1", "tasks": [
                "degrees to radians converter",
                "radians to degrees converter"
            ]}
        ]

        self.write(LayoutGenerator.gen_header())
        self.write("<ul>")
        for category in categories_list:
            self.write('<li><a href="' + category["uri"] + '">')
            self.write(category["name"])
            self.write('</a></li>')
            self.write("<ul>")
            for task in category["tasks"]:
                self.write("<li>" + task + "</li>")
            self.write("</ul>")
            self.write("<li>---</li>")
        self.write("</ul>")
