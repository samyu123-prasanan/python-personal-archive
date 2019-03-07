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
 

import pathlib
#import pathlib

#from os import path

def startpy():
    

    file = pathlib.Path("article 15.docx")
    if file.exists ():
        print ("File exist")
    else:
        print ("File not exist")


     #path = pathlib.Path('db222.txt')
     #path.exists()
    #file = os.path.isfile('E:\tact\jff\new1.txt')
    #print ("file exist:"+str(path.exists('E:\tact\jff\new1.txt')))
    #print (file)


if __name__ == '__main__':
    startpy()