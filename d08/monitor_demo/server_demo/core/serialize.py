#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import global_settings

import pickle,time

from conf import hosts


def host_config_serializer(host_ip):
    applied_services = []
    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)    
    print(applied_services)
        
if __name__ =='__main__':
    host_config_serializer('192.168.77.119')