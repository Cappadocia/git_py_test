#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import global_settings

import pickle,time

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
        
        
if __name__ =='__main__':
    host_config_serializer('192.168.77.119')
        
        
         
