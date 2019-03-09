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
 
from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():

    youtube_link  = request.form.get("youtube_link")
    emotion  = request.form.get("emotion")
    hint  = request.form.get("hint")

    

    print('link : ', youtube_link)

    result = {
        'apiresult' : 0,
        'apimessage' : 'OK',

        'youtube_link' : youtube_link,
        'emotion' : emotion,
        'hint' : hint
    }

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()