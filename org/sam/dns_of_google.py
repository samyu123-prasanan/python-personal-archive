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
 
import socket
def startpy():
   
   address = socket.gethostbyname('google.com')
   print "Address=",address

if __name__ == '__main__':
    startpy()
    