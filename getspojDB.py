#!/usr/bin/python2
import urllib
import re
import os
def postprocess(entry):
       #remove unnecessary <*>
       retstr=""
       adder=0;
       for i in range(len(entry)):
         if entry[i]=='<':
	   adder=1
	   continue
	 if entry[i]=='>':
	   adder=0
	   continue
	 if adder==0:
	   retstr=retstr+entry[i]
       return retstr
def extractdata(entry):
       # To get only the text content in <tr></tr>
       while "</" in entry:
        entry=re.findall(">.*</",entry)[0][1:-2]
       entry=postprocess(entry)
       return entry
def getspojDB():
   dataline=""
   DB=""
   #TO CHECK IF NEW PROBLEM IS ADDED
   checker={}
   cur=-50
   while 1==1:
     cur=cur+50
     url="http://www.spoj.pl/problems/classical/sort=0,start="+str(cur);
     page=urllib.urlopen(url)
     addval=0
     for line in page.read().split('\n'):
        if "<tr class=\"problemrow\">" in line:
          addval=1
        if addval==1:     
          dataline=dataline+line
        if ("</" in line ):
          dataline=dataline+"\n"
        if ("</tr>" in line) and addval==1:
           addval=0
           entryval=[]
           NAME=""
           ID=""
           CODE=""
           USERS=""
           ACC=""
           for entry in dataline.split('\n'):
               if "\"/problems/" in entry:
	            NAME=extractdata(entry) 
	       if "class=\"problemrow\"" in entry:
	            ID=extractdata(entry)
	       if "\"/submit/" in entry:
	            CODE=extractdata(entry)
	       if "\"/ranks/" in entry:
	            USERS=extractdata(entry)
               if "\"/status/" in entry:
	            ACC=extractdata(entry)
           dataline=""
	   if CODE in checker:
                return DB
           print "GOT A PROBLEM! ID:",ID," NAME:",NAME," CODE:",CODE," USERS:",USERS," ACC:",ACC
           checker[CODE]=1
	   DB=DB+ID+"|"+NAME+"|"+CODE+"|"+USERS+"|"+ACC+"\n"
     page.close()
if(__name__=="__main__"):
   data=getspojDB()
   print "Refreshing Data"
   print "Getting list of problems from SPOJ.pl"
   phyfile=open("SPOJPROB","w+")
   phyfile.writelines(data)
   phyfile.close()  
   print "Getting SPOJ Classifier list"
   os.system("rm -rf SPOJCLASS")
   os.system("wget http://web.iiit.ac.in/~srinivasan.l/extras/SPOJCLASS")
