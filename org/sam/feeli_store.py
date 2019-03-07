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

def store_songs():
    song1 = {
                'youtube_link':'https://www.youtube.com/watch?v=mytLRy32Viw', 
                'emotion': 'Happiness',
                'user_hint': 'Chennai girl'
            } 
    song_list = []
    song_list.append(song1)


    song2 = {
                'youtube_link':'https://www.youtube.com/watch?v=f3FFOBrMmdg', 
                'emotion': 'Depressed',
                'user_hint': 'The gurl with a macbook'
            } 
    song_list.append(song2)


    song3 = {
                'youtube_link':'https://www.youtube.com/watch?v=7C2z4GqqS5E', 
                'emotion': 'I feel a burning rage in this song',
                'user_hint': 'Adai love girl'
            } 
    song_list.append(song3)


    file_Name = "FeelI"

    fileObject = open(file_Name,'wb') 

    # this writes the object a to the
    # file named 'testfile'
    pickle.dump(song_list,fileObject)   

 

def read_songs():

    file_Name = 'FeelI'

    fileObject = open(file_Name,'r')  

    song_list = pickle.load(fileObject)  

    #print(song_list)     

    for song in song_list:
        #print(song)
        #print(type(song))
        print('Song  ['+str(song["youtube_link"])+'] liked by '+str(song["user_hint"]))

if __name__ == '__main__':
    #store_songs()

    read_songs()