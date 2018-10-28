import tornado.ioloop
import tornado.web
from site.nav import IndexHandler


def make_tornado_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
    ])


if __name__ == "__main__":
    app = make_tornado_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
