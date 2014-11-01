

import os




import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer

HOST = 'localhost'
PORT = 8880

global N
N = 8

import json
import time
import requests
import datetime
import dateutil

from collections import defaultdict

import numpy as np

import matplotlib.pyplot as plt
#from mpld3 import fig_to_html, fig_to_d3, show_d3

class set_params(tornado.web.RequestHandler):
    def get(self, *args):
        self.post(*args)

    def post(self, *args):
        """
        """
        global N

        tmp = int(self.get_argument('N'))
        if tmp<30 and tmp>0:
            N = tmp

class plot_ug(tornado.web.RequestHandler):
    def get(self, *args):
        self.post(*args)
        #self.write("not implemented yet")

    def post(self, *args):
        """ 
        
        """
        
        os.system('./graphgen ' + str(N))

        self.write('<!DOCTYPE html><html><body>')
        self.write('<img src=\"./deneme_orig.png\">')
        self.write('</body></html>')

        #self.add_header('Content-Type', 'application/json')

class plot_mst(tornado.web.RequestHandler):
    def get(self, *args):
        self.post(*args)
        #self.write("not implemented yet")

    def post(self, *args):
        """ 
        
        """
        
        self.write('<!DOCTYPE html><html><body>')
        self.write('<img src=\"./deneme.png\">')
        self.write('</body></html>')

        #self.add_header('Content-Type', 'application/json')


DEBUG = True
DIRNAME = os.path.dirname(__file__)
STATIC_PATH = os.path.join(DIRNAME, '.')


routes_config = [
    (r"/set_params", set_params),
    (r"/plot_ug", plot_ug),
    (r"/plot_mst", plot_mst),
    (r"/(.*\.png)", tornado.web.StaticFileHandler,{"path": "." }),
]


application = tornado.web.Application(routes_config)

def start():
    print "GraphGen Server Starting on port %s" % PORT
    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
    return application

if __name__ == "__main__":
    start()
