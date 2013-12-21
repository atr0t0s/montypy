'''
Created on Dec 21, 2013

@author: George Violaris http://www.montypy.org
'''
import cherrypy
class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())