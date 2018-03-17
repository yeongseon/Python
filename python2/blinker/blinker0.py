# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:24:01 2018

@author: I338162
"""

from blinker import signal
started = signal('round-started')
terminate = signal('terminal')

def each(round):
    print("Round %s!" % round)
    
started.connect(each)

def round_two(round):
    print("This is round two.")
    
started.connect(round_two, sender='test')

for round in range(1, 4):
    started.send(round)
    
started.send('test')

terminate.send()