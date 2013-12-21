import cherrypy
import os

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
        print "Debug"
        return password


config = {'/web': {'tools.staticdir.on': True, 'tools.staticdir.dir': MEDIA_DIR, }}

root = LoginPage()