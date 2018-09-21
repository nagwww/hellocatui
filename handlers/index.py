from handlers.base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
#        self.write("Hello, world")
        self.render("../templates/index.html")
