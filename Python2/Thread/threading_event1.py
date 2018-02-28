# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:39:19 2018

@author: I338162
"""
import threading

stop_lock = threading.Event()

print(stop_lock.is_set())

stop_lock.set()

print(stop_lock.is_set())