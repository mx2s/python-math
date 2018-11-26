import tornado.ioloop
import tornado.web

from pages.geometry_1 import Geometry1Handler
from pages.index_handler import IndexHandler


def make_tornado_app():
    return tornado.web.Application(
        [
            (r"/", IndexHandler),
            (r"/geometry_1", Geometry1Handler)
        ]
    )

if __name__ == "__main__":
    app = make_tornado_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
