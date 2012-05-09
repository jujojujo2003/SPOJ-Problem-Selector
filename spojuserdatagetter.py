#!/usr/bin/python2
import urllib
import os
import string
import re
import getspojDB
def getter(username):
  url="http://www.spoj.pl/status/"+username+"/signedlist/"
  print "Fetching data"
  userpage=urllib.urlopen(url).read().split('\n')
  ACCED={}
  WAED={}
  enabledata=0
  for line in userpage:
       if enabledata==1 and "\----------------------------------" in line:
          enabledata=0
       if "---------------" in line:
           continue
       if enabledata==1:
           data=line
           data=data.replace("|"," ")
           data=data.split()
           if(len(data)>=5):
              if data[4] == "AC" or data[4].isdigit():
                  ACCED[data[3]]=1
                  WAED[data[3]]=0
              elif data[3] in WAED:
                  WAED[data[3]]=WAED[data[3]]+1
       if "BEGIN OF DATA" in line:
           print "Reading Data"
       if "ID" in line and "DATE" in line and  "PROBLEM" in line and  "RESULT" in line and  "TIME" in line:
           enabledata=1
  return WAED
           
if __name__=='__main__':
  getter("haha")
