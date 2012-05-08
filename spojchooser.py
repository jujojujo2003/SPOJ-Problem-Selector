#!/usr/bin/python2
import urllib
import os
import string
import re
import getspojDB
def main():
  print "Enter Your SPOJ User ID:"
  username=raw_input()
  url="http://www.spoj.pl/users/"+username+"/signedlist/"
  userpage=urllib.urlopen(url).read().split('\n')
  NAME=""
  RANK=""
  PROBLEMS=[]
  for line in userpage:
      if "<H3>" in line:
            NAME=line
            NAME=string.replace(NAME,"<H3>","")
            NAME=string.replace(NAME,"</H3>","")
            NAME=string.replace(NAME,"'s user data","")
            NAME=string.replace(NAME," ","")
            NAME=string.replace(NAME,"	","")
            NAME=NAME.split()[0]
      if "Current world rank:" in line:
            RANK=line
            RANK=getspojDB.extractdata(re.findall("<a .*</a",RANK)[0])
      if "/status/" in line:
            TEMP=line
            TEMP=getspojDB.extractdata(TEMP)
            print TEMP
if __name__=='__main__':
  main()
