#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: samyuktha

Source:
    
'''

# Import necessary modules
 

import os

def startpy():
    b = os.path.getsize("E://tact//daily_log.txt")
    print(b)    


if __name__ == '__main__':
    startpy()