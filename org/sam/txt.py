import os 
f=open("new1.txt","r")
if f.mode=='r':
  contents=f.read()
  print(contents)