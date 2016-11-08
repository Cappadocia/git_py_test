#!/usr/bin/env python
#coding:utf-8

from wsgiref.simple_server import make_server

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'

#     #获取用户的URL
#     userUrl = environ['PATH_INFO']
#     #跟进URL不同返回不同结果
#     if userUrl =='/index/':
#         return'<h1>index</h1>'
#     elif userUrl == '/login/':
#         return'<h1>login</h1>'
#     else:
#         return '<h1>404 404</h1>'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print ("Serving HTTP on port 8000...")
    httpd.serve_forever()