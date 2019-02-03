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
import re 


def startpy(email):
    
    if len(email) > 7:
        matched = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
        if matched != False:
            print ("True")
        else:
            print ("False")
    else:
        print "This is not a valid email address"
    
   
from __builtin__ import True
     


if __name__ == '__main__':
    startpy("wordbay99@gmail.com")