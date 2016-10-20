#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import redishelper
import pickle
import time

from plugin import plugin_api

#host_ip = '本机IP地址'
host_ip = '192.168.77.119'

class MonitorClient(object):
    def __init__(self,server,port):
        self.server = server
        self.port = port
        self.configs = {}
        #建立redis链接
        self.redis = Redishelper()
        
        
    #获取配置信息   
    def get_configs(self):
        config = self.redis.get('HostConfig::s%' %host_ip)
        if config:
            self.configs = pickle.load(config)
            return True
    #调用插件
    def handle(self):
        if self.get_configs():
            print('----going to monitor services---------',self.configs)
            #处理不同时间需求配置的死循环
            while True:
                for service_name,val in self.configs['services'].items():
                    interval,plugin_name,last_check = val
                    if time.time() - last_check >= interval:
                    #need to kick off the next run
                        t = threading.Thread(target=self.task,args=[service_name,plugin_name])
                        t.start()
                        #更新last_check 时间
                        self.configs['services'][service_name][2] = time.time()
                    else:
                        next_run_time = interval - (time.time() - last_check)
                        print('%s will be run in next s% seconds' %(service_name,next_run_time))
                time.sleep(1)       
        else:
            print('---could not find any configurations for this host----')
    
    def format_msg(self,key,value):
        msg  = {key:value}
        return pickle.dumps(msg)
    
    
    def task(self,service_name,plugin_name):
        print( '----going to run service ',service_name,plugin_name)
        func = getattr(plugin_api,plugin_name)
        result = func()
        #发布到服务端，发布频道是87.7，序列号发布值
        msg = self.format_msg('report_service_data', {'ip':host_ip,
                                                      'service_name':service_name,
                                                      'data':result,})
        #self.redis.publish(pickle.dumps(result))
        self.redis.publisc(msg)
    def run(self):
        self.handle()
    
    
if __name__ =='__main__':
    cli = MonitorClient('yourMonitorserver','port')
    cli.run()
    
    