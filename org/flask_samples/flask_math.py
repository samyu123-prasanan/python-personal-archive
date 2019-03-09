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
 
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Mahiba Sharon"


@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    c = a + b
    
    return "Serena " + str(c)

if __name__ == '__main__':
    app.run()