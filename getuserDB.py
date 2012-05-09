#!/usr/bin/python2
import urllib
import re
import spojuserdatagetter
import signal
import sys
breaker=0
AVGACC={}

def sig_handler(signal,frame):
  breaker=1
  print "Set Breaker"
  FILE=open("SPOJDIFF","w+")
  for prob in AVGACC:
       FILE.write(prob+" "+str(AVGACC[prob])+"\n")
  FILE.close()
  sys.exit(0)  



def addtodict(uname):
     PROBS=spojuserdatagetter.getter(uname)
     for prob in PROBS:
         if prob in AVGACC:
                AVGACC[prob]=(AVGACC[prob]*1.0+PROBS[prob]*1.0)/2.0
         else:
                AVGACC[prob]=PROBS[prob]*1.0
     print "Done for ",uname

def ranker():
  USERS={}
  signal.signal(signal.SIGINT,sig_handler)
  userno=0
  breaker=0
  while 1==1:
   url="http://www.spoj.pl/ranks/users/start="+str(max(0,len(USERS)))
   urlpage=urllib.urlopen(url).read().split('\n')
   for line in urlpage:
       if "/users/" in line:
           uname=re.findall("/users/.*\"",line)[0][7:-1]
#          print uname
           if "\"" in uname:
              pass
           elif uname in USERS:
              breaker=1
              break
           else:
              USERS[uname]=1
#             Unique username found
              print "ADDED ",uname," TOTAL: ",len(USERS)
              addtodict(uname)
   if breaker==1:
       break
  FILE=open("SPOJDIFF","w+")
  for prob in AVGACC:
       FILE.write(prob+" "+AVGACC[prob]+"\n")
  FILE.close()


if __name__=='__main__':
   ranker()
