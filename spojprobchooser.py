#!/usr/bin/python2
import re
import math
import spojuserdatagetter
SPOJCLASS={}
SPOJDIFF={}
TAGLIST={}
PROBLIST={}
def funtosolve(PROBS,minormax):
    SCORE={}
    for prob in SPOJCLASS:
      SCORE[prob]=0
      for tags in SPOJCLASS[prob]:
       if tags in TAGLIST:
        SCORE[prob]=SCORE[prob]+TAGLIST[tags]
    items=SCORE.items()
    items=[(float(value),key) for key,value in items]
    items.sort()
    items.reverse()
    
    PROBLEMSCORE=""
    for value,key in items:
      if key not in PROBS and PROBLEMSCORE=="":
           PROBLEMSCORE=value
      elif key not in PROBS and PROBLEMSCORE!="":
           if value >PROBLEMSCORE:
              PROBLEMSCORE=value


    SELECTEDMAX=[]
    SELECTEDMIN=[]
    for value,key in items:
       if value==PROBLEMSCORE and key not in PROBS:
         SELECTEDMAX=SELECTEDMAX+[key]
    
    PROBLEMSCORE=""
    for value,key in items:
      if key not in PROBS and PROBLEMSCORE=="":
           PROBLEMSCORE=value
      elif key not in PROBS and PROBLEMSCORE!="":
           if value <PROBLEMSCORE:
              PROBLEMSCORE=value

   
    for value,key in items:
       if value==PROBLEMSCORE and key not in PROBS:
         SELECTEDMIN=SELECTEDMIN+[key]
    if len(SELECTEDMIN)<=0 or len(SELECTEDMAX)<=0 :
         print "Sorry! Please try solving more problems! I cannot get what type of problems you like \n form the list of problems you have solved.!"
         return "" 
    THECHOSENONEMAX=SELECTEDMAX[0]
    THECHOSENACCMAX=SPOJDIFF[THECHOSENONEMAX]
    THECHOSENONEMIN=SELECTEDMIN[0]
    THECHOSENACCMIN=SPOJDIFF[THECHOSENONEMIN]
    for entry in SELECTEDMAX:
        if SPOJDIFF[entry] < THECHOSENACCMAX:
                 THECHOSENACCMAX=SPOJDIFF[entry]
                 THECHOSENONEMAX=entry
    for entry in SELECTEDMIN:
        if SPOJDIFF[entry] < THECHOSENACCMIN:
                 THECHOSENACCMIN=SPOJDIFF[entry]
                 THECHOSENONEMIN=entry
    if "MIN" in minormax:
         return THECHOSENONEMIN,SELECTEDMAX
    else:
         return THECHOSENONEMAX,SELECTEDMIN
      
def difficultybased(PROBS):
    print "Enter your desired difficulty level(0-100)"
    LEVEL=float(raw_input())
    items=PROBLIST.items()
    items=[(float(value),key) for key,value in items]
    item2=SPOJDIFF.items()
    item2=[(float(value),key) for key,value in item2]
    item2.sort()
    MIN=item2[0][0]
    MAX=item2[len(item2)-1][0]
    item3={}
    #Normalize acc rates
    for tuples in item2:
        score=((tuples[0]-MIN*1.0)/(MAX-MIN*1.0))*100
        item3[tuples[1]]=score
    SELECTEDONES=[]
    for i in items:
       if math.fabs(i[0]-LEVEL+max(DIFFICULTYLEVEL,5)) <= 8.0 and i[1] not in PROBS:
         SELECTEDONES=SELECTEDONES+[i[1]]
    if len(SELECTEDONES)<=0:
           print "No problems with your difficulty level found "
           return ""
    THECHOSENONE=SELECTEDONES[0]
    THECHOSENACC=100
    if THECHOSENONE in SPOJDIFF:
       THECHOSENACC=SPOJDIFF[THECHOSENONE]
    for i in SELECTEDONES:
       if i in item3:
         if THECHOSENACC > item3[i]:
           THECHOSENONE=i
           THECHOSENACC=item3[i] 
    return THECHOSENONE,SELECTEDONES
def main():
    global DIFFICULTYLEVEL
    DIFFICULTYLEVEL=0
    print "Enter you SPOJ username:"
    username=raw_input()
    print "Getting your solved problem list"
    PROBS=spojuserdatagetter.getter(username)
    FILE=open("SPOJCLASS","r")
    FILECONTENT=FILE.read()
    FILECONTENT=FILECONTENT.split('\n')
    for i in FILECONTENT:
        i=i.split()
        if len(i) >= 2:
           SPOJCLASS[i[0]]=i[1:]
    FILE.close()
    FILE=open("SPOJDIFF","r")
    FILECONTENT=FILE.read()
    FILECONTENT=FILECONTENT.split('\n')
    for i in FILECONTENT:
        i=i.split()
        if len(i) >= 2:
           SPOJDIFF[i[0]]=i[1]
    FILE.close()
    FILE=open("SPOJPROB","r")
    FILECONTENT=FILE.read()
    FILECONTENT=FILECONTENT.split('\n')
    for i in FILECONTENT:
        i=i.split('|')
        if len(i)>=3:
         pname=i[2]
         PROBLIST[pname]=i[4]
    for prob in PROBS:
       if prob in SPOJCLASS:
          TAGS=SPOJCLASS[prob]
          for tag in TAGS:
             if tag not in TAGLIST:
                   TAGLIST[tag]=1
             else: 
                   TAGLIST[tag]=TAGLIST[tag]+1
    for prob in PROBS:
       if prob in SPOJDIFF:
        DIFFICULTYLEVEL=(DIFFICULTYLEVEL+(PROBS[prob]-float(SPOJDIFF[prob])))/2.0
    while 1==1:
     print "Your Difficulty Level:",DIFFICULTYLEVEL
     print "If difficulty level is 0, you are average, if its less than 0 , you are above average  and its greater than 0 , you are below average!"
     print "1) Pick A Fun to Solve problem"
     print "2) Pick A Problem to improve my weakness"
     print "3) Pick Problem Based on Difficulty Level"
     print "4) Exit"
     print "Enter Choice "
     needed=raw_input()
     CHOSEN=""
     SELECTED=[]
     if "1" in needed:
        CHOSEN,SELECTED=funtosolve(PROBS,"MAX")
     elif "2" in needed:
        CHOSEN,SELECTED=funtosolve(PROBS,"MIN")
     elif "3" in needed:
        CHOSEN,SELECTED=difficultybased(PROBS)
     else:
        break
     print "\n\n\nWe found the best match ! Please try the problem at this url","http://www.spoj.pl/problems/"+CHOSEN+"/"
     print "You can also try these"
     for i in range(min(5,len(SELECTED))):
        print "http://www.spoj.pl/problems/"+SELECTED[i]+"/"
     print "\n\n\n"
if __name__ == '__main__':
    main()
