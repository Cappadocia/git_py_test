#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#将项目目录加入环境变量

import os,sys 
base_dir = os.path.dirname(os.path.dirname(__file__))
print(base_dir)
sys.path.append(base_dir)