from xml.sax import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):pass
parse('website.xml', TestHandler())
def startElemenet(self, name, attrs):
    print name,attrs.keys()
