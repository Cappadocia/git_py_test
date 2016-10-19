#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#服务的标准模板
import generic  
from data_process import avg,hit,last

class cpu(generic.BaseService):
    def __init__(self):
        super(cpu,self).__init__()
        self.name = 'linux_cpu'
        self.interval = 30
        self.plugin_name = 'get_cpu_status'
        self.truggers = {
                'idle':{'func':avg,
                        'minutes':15,
                        'operator':'lt',
                        #'threshold':0,
                        'warning':20,
                        'critical':5,
                        'data_type':'percentage'
                        },
                'iowait':{'func':hit,
                        'minutes':10,
                        'operator':'gt',
                        'threshold':3,
                        'warning':50,
                        'critical':80,
                        'data_type':'int'
                        },
                         }
        
class memory(generic.BaseService):
    def __init__(self):
        super(memory,self).__init__()
        self.name = 'linux_memory'
        self.interval = 60
        self.plugin_name = 'get_memory_info'
        self.truggers = {
                'idle':{'func':avg,
                        'minutes':15,
                        'operator':'gt',
                        #'threshold':0,
                        'warning':80,
                        'critical':90,
                        'data_type':'percentage'
                        }
                         }
        
        
        
if __name__ == '__main__':
    c = cpu()
    print(c.name,c.interval,c.plugin_name)
    
    