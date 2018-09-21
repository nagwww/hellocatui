from handlers.index import IndexHandler
from handlers.health import HealthHandler
from handlers.users import GetUserHandler
import tornado.web

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/healthcheck", HealthHandler),
        (r'/api/v1/get_users', GetUserHandler),
        (r'/api/v1/get_users/(.*)', GetUserHandler),
    ])
