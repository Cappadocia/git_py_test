#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def handle_request(client):
    buf = client.recv(1024)
    #HTTP协议状态码
    #client.send("HTTP/1.1 200 OK\r\n")
    #请求头，页面展示什么类型
    #client.send('Content-Type:text/html\r\n\r\n')
    client.send(bytes('hello,server',encoding = 'utf8'))
    
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',9080))
    sock.listen(5)
    
    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()
        
if __name__ =='__main__':
    main()
    
    