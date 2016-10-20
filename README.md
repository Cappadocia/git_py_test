# -*- coding: utf-8 -*-
# git_py_test

#增加d08代码记录

#增加monitor_demo模块

新增目录结构
server 
     --conf  相关配置信息
     		--services 相应监控项
                    --data_process.py
                    --generic.py 通用数据
                    --linux.py
     		--__init__.py
     		--hosts.py
     		--templates.py
     --core 处理监控数据的相关文件
     		--__init__.py
     		--action_process.py
     		--data_sucker.py
     		--global_setting.py
     		--main_server.py
     		--redishelper.py
     		--seroalize.py
client
     --plugin
     --__init__.py
     --client.py
     --redishelper.py
     
