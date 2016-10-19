#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#通用监控项
class BaseService(object):
    def __init__(self):
        #监控名
        self.name = 'BaseService'
        #监控间隔300秒
        self.interval = 300
        self.last_time = 0
        #监控插件化，对应相应的插件名
        self.plugin_name ='your_plugin_name'
        #设置监控阈值（监控指标）
        self.triggers = {}