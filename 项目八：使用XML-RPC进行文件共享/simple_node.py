from xmlrpclib import ServerProxy
from os.path import join, isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys

MAX_HISTORY_LENGTH = 6

OK = 1
FAIL = 2
EMPTY = ''

def getPort(url):
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])

class Node:
    """
    P2P中的节点 
    """
    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()
    def query(self, query, history=[])
        code, data = self._handle(query)
        if code == OK:
            return code, data
        else: 
            history = history + [self.url]
            if len(histoy) >= MAX_HISTORYU_LENGTH:
            return FAIL, EMPTY        
        return self._broadcast(query, history)
        


def _handle(self, query):
    dir = self.dirname
    name = join(dir, query)
    if not isfile(name): return FAIL, EMPTY
    return OK, open(name).read()


def hello(self, other):
    self.known.add(other)
    return OK

def fetch(self, query, secret):
    if secret != self.secret :RETURN FAIL
    code, data = self.query(query)
    if code == OK:
        f = open(join(self.dirname),'w')
        f.write(data)
        f.close()
        return OK
    else: 
        return FAIL

def _start(self):
    s = SimpleXMLRPCServer(("", getPort(self.url)), logRequests=False)
    s.register_instance(self)
    s.erver_forever()

def _broadcast(self, query, history):
    for ther in self.knoen.copy():
        if other in history: continue
        try:
            s = ServerProxy(other)
            code, data =s.query(query, history)
            if code == OK:
                return code, data
        except:
            self.known.remove(other)
    return FAIL, EMPTY

def main():
    url, directory, secret = sys.argv[1:]
    n = Node(url, directory, secret)
    n,_start
if __name__== '__main__':main()























