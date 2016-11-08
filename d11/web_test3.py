#!/usr/bin/env python
#coding:utf-8
#自定义web框架，基于wsgiref
from wsgiref.simple_server import make_server

def index():
    return 'index'

def login():
    return 'login'

def routers():
    
    urlpatterns = (
        ('/index/',index),
        ('/login/',login),
    )
    
    return urlpatterns

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break 
    if func:
        return func()
    else:
        return '404 not found'
    
if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print ("Serving HTTP on port 8000...")
    httpd.serve_forever()