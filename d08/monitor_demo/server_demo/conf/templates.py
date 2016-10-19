#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from services import linux

class BaseTemplate(object):
    def __init__(self):
        self.name = 'YourTemplateName'
        self.group_name = 'YourGroupName'
        self.hosts = []
        #监控哪些服务
        self.services = []

#基础BaseTemplate        
class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.services =[
                linux.cpu,
                linux.memory
                        ]
#测试用例
# if __name__ =='__main':
#     t = LinuxTemplate()
#     t.hosts = ['192.168.77.119']
#     for service in t.services:
#         print(service.name,service.triggers)