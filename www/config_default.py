#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config_default.py
# @Author: lvconl
# @Date  : 18-1-27
#@Software : PyCharm


configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}