import cherrypy

class LindenmayerServer(object):
    @cherrypy.expose
    def generate(self):
        return "yes"