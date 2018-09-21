import tornado.web

class HealthHandler(tornado.web.RequestHandler):
    async def get(self):
       self.write("Yoo! I am here")
