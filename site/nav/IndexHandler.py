from abc import ABC
import tornado.web

from modules.site.layout_generator import LayoutGenerator


class IndexHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        categories_list = [
            {"name": "category", "uri": "/someStuff"}
        ]

        self.write(LayoutGenerator.gen_header())
        self.write("<ul>")
        for category in categories_list:
            self.write('<li><a href="' + category["uri"] + '">')
            self.write(category["name"])
            self.write('</a></li')
        self.write("</ul>")
