# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:46:47 2017

@author: I338162
"""

from threading import Thread, Event

class ThreadTester(Thread):
    
    def __init__(self):
        super(ThreadTester, self).__init__()
        self._stop = Event()
        
    def run(self):
        self._stop.wait(5)
        
        try:
            while not self.stopped:
                self._test()
            
            self._stop.wait(5)
        except Exception as exc:
            print(exc)
        
    def stop(self):
        self._stop.set()
    
    @property
    def stopped(self):
        return self._stop.isSet()

    def _test(self):
        for i in xrange(1, 10):
            print("start...." + str(i))
        
        
thread_tester = ThreadTester()
thread_tester.start()
