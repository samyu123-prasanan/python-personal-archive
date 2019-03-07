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
 
import pickle

def startpy():
   

    a = ['test value','test value 2','test value 3']

    file_Name = "Sam_wordbay"
    # open the file for writing
    fileObject = open(file_Name,'wb') 

    # this writes the object a to the
    # file named 'testfile'
    pickle.dump(a,fileObject)   

    # here we close the fileObject
    fileObject.close()
    # we open the file for reading
    fileObject = open(file_Name,'r')  
    # load the object from the file into var b
    b = pickle.load(fileObject)  
    print(a==b)
    


if __name__ == '__main__':
    startpy()