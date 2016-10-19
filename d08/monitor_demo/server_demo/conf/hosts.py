#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import templates

#实例化
g1 = templates.LinuxTemplate()
g1.group_name = 'Test groups'
g1.hosts = ['192.168.77.119','192.168.47.191']

g2 = templates.LinuxTemplate()
g2.group_name = 'puppet server groups'
g2.hosts = ['192.168.47.189']


g3 = templates.NetworkTemplate()
g3.group_name = 'puppet server groups'
g3.hosts = ['192.168.47.189']


monitored_groups = [g1,g2]

