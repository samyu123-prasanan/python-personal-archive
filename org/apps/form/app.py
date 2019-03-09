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
import pickle


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

    song_list = read_songs()

    result = {
        'apiresult' : 0,
        'apimessage' : 'OK',

        'songs' : song_list
    }

    return render_template('index.html', result=result)

def read_songs():

    file_Name = 'E:\\tact\\python-personal-archive\\FeelI'

    fileObject = open(file_Name,'r')  

    song_list = pickle.load(fileObject)  

    #print(song_list)     

    for song in song_list:
        #print(song)
        #print(type(song))
        print('Song  ['+str(song["youtube_link"])+'] liked by '+str(song["user_hint"]))    

    return song_list


if __name__ == '__main__':
    app.run()