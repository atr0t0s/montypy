import cherrypy
import router

cherrypy.config.update(
    {'server.socket_host': '0.0.0.0' } )
cherrypy.quickstart(router.LoginPage())