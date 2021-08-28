#define module Hello:
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:26:28 2021

@author: hanyeh00
"""
class Hello():
    def hello(self,name):
        self.name=name
        print(f"hello {self.name}")
        
"""
import module:
first save class Hello in seprated file name ,hello.py,
then import it"""

import hello
t=hello.Hello() # define a class
t.hello("ALi")

        
