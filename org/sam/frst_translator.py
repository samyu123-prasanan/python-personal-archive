#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages
    http://docs.python-requests.org/en/master/
    https://translate.yandex.com/developers/keys
    
'''

# Import necessary modules
import requests
import json
import sys

KEY = 'trnsl.1.1.20190319T222338Z.d93706c419b2d04f.80bc5f0f6f99967ee34e80c3612898353f492d06'
API_BASE = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def startpy():

    word = 'World'

    #rint('len of argv : ', len(sys.argv))

    if(len(sys.argv) > 1):
        word = sys.argv[1]
    
    fr_content = translate_en_to_fr(word)
    sp_content = translate_en_to_sp(word)
    tu_content = translate_en_to_tu(word)

    print(word)
    print(fr_content)
    print(sp_content)
    print(tu_content)


def translate_en_to_sp(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-es')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_tu(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-tr')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_fr(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-fr')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content



if __name__ == '__main__':
    startpy()