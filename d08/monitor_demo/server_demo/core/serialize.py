#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import global_settings

import pickle,time
from redishelper import Redishelper

from conf import hosts


def host_config_serializer(host_ip):
#     applied_services = []
#     
#     for group in hosts.monitored_groups:
#         if host_ip in group.hosts:
#             applied_services.extend(group.services)    
#     print(applied_services)
#         
# if __name__ =='__main__':
#     host_config_serializer('192.168.77.119')

    applied_services = []
    #不确定configs 里会不会加其他，为以后留扩展余地
    configs = {
                'services':{},
                #'refresh_configs_interval':
                }
     
    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)    
    applied_services = set(applied_services)
    
    for service in applied_services:
        #把取出来的类实例化
        service = service()
        configs['services'][service.name] = [service.interval,service.plugin_name,0]
        
    return configs

def flush_all_host_configs_into_redis():
    applied_hosts = []
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    #去重
    applied_hosts = set(applied_hosts)
    
    for host_ip in applied_hosts:
        host_config = host_config_serializer(host_ip)
        key = 'HostConfig::s%' %host_ip
        redis.set(key,pickle.dumps(host_config))
    return True
if __name__ =='__main__':
    #host_config_serializer('192.168.77.119')
    flush_all_host_configs_into_redis()
        
        
         
