'''
Created on Dec 21, 2013

@author: George Violaris http://www.montypy.org

Just testing that the CherryPy server can run on the system
'''
import cherrypy
class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())