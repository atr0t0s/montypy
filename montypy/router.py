import cherrypy
import os
import platform
import socket
import json

MEDIA_DIR = os.path.join(os.path.abspath("."), u"web")

#routing to other pages
class OtherPage(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index2.html'))

class LoginPage(object):
    otherpage = OtherPage()
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index.html'))

    @cherrypy.expose
    def request(self, username, password):
        #print "Debug"
        return password
    
    @cherrypy.expose
    def sysinfo(self):
        sysinfo = [platform.system(),platform.release(),platform.version(),socket.gethostname()]
        return json.dumps(  [{  
                                "System"    : sysinfo[0], 
                                "Release"   : sysinfo[1], 
                                "Version"   : sysinfo[2],
                                "Hostname"  : sysinfo[3]
                            }])

config = {'/web': {'tools.staticdir.on': True, 'tools.staticdir.dir': MEDIA_DIR, }}

root = LoginPage()