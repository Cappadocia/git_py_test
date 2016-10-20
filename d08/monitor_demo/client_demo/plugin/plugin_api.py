#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import load,cpu,memory

def get_load_info():
    return load.monitor()

def get_cpu_status():
    return cpu.monitor()

def get_memory_info():
    return memory.monitor()

def get_network_info():
    return memory.monitor()