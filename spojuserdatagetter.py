#!/usr/bin/python2
import urllib
import os
import string
import re
import getspojDB
def main():
  print "Enter Your SPOJ User ID:"
  username=raw_input()
  url="http://www.spoj.pl/status/"+username+"/signedlist/"
  userpage=urllib.urlopen(url).read().split('\n')
  PROBLEMS=[]
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
           print data
       if "BEGIN OF DATA" in line:
           print "Reading Data"
       if "ID" in line and "DATE" in line and  "PROBLEM" in line and  "RESULT" in line and  "TIME" in line:
           enabledata=1
           
if __name__=='__main__':
  main()
