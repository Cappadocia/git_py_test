#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# from conf.services import generic  
# from conf.services import data_process
# 
# class nic(generic.BaseService):
#     def __init__(self):
#         super(nic,self).__init__()
#         self.name = 'nic_network'
#         self.interval = 120
#         self.plugin_name = 'get_network_info'
#         self.truggers = {
#                 'in':{'func':avg,
#                         'minutes':15,
#                         'operator':'gt',
#                         #'threshold':0,
#                         'warning':80,
#                         'critical':90,
#                         'data_type':'percentage'
#                         }
#                          }