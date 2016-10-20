#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pickle
import serialize

def action_process(server_instance,msg):
    #接收msg
    msg = pickle.loads(msg[2])
    print(msg)
    #字典格式msg,字典中只有一个key,这个方法把数据打上时间戳
    func_name = msg.keys()[0]
    func = getattr(serialize,func_name)
    func(server_instance,msg[func_name])