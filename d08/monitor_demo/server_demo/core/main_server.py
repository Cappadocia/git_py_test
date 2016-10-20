#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#服务器端接收程序

import global_settings
from redishelper import RedisHelper
import serialize

import action_process

class MonitorServer(object):
    def __init__(self,ip,port):
        #本机IP
        self.ip = ip
        #本机端口
        self.port = port
        #self.hosts = serialize.all_host_configs()
        self.redis = RedisHelper()
        
    def handle(self):
        redis_sub = self.redis.subscribe()
        #redis_sub.parse_response()
        while True:
            msg = redis_sub.parse_response()
            #收到消息就打印，没有就堵塞
            print('recv:',msg)
            #收到丢给action_process
            action_process.action_process(self,msg)
            print('-----waiting for new msg------')
            
            for host,val in self.hosts['hosts'].items():
                print(host,val)
                
    def run(self):
        print('--------starting monitor server -------')
        self.handle()
        
    def process(self):
        pass
    
if __name__ =='__main__':
    #redis ip port
    s =  MonitorServer('0.0.0.0','8000')
    s.run()
            