import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        host = cherrypy.request.headers['Host']
        return "You have successfully reached " + host
    
cherrypy.config.update(
    {'server.socket_host': '0.0.0.0' } )
cherrypy.quickstart(HelloWorld())