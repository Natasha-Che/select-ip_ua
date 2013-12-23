#!/usr/bin/python                                                                                                                                                    

import random;

file=open('/Users/natasha.che/seawaves')

d1={ }

for line in file:
    line = line.rstrip().split("\t")
    d1.setdefault(line[0],set( )).add(line[2])

file.close()

file=open('/Users/natasha.che/seawaves')

d2={ }
for line in file:
    line = line.rstrip().split("\t")
    d2.setdefault(line[0],set( )).add(line[5])

file.close()

keylist=d1.keys()
keylist.sort()
keylist2=d2.keys()
keylist2.sort()
idlist=[]
for key2 in keylist2:
  if len(d2[key2])==1:
     idlist.append(key2)

idlist2=[]

for key2 in keylist2:
    if len(d2[key2])>1:
       idlist2.append(key2)
       

idlist3=[]


names=set(name.strip() for name in idlist)

for key in keylist:
    if key.strip() in names and len(list(d1[key]))==1:
          idlist3.append(list(d1[key])[0])

idlist4=[]

nams=set(nam.strip() for nam in idlist2)

for key in keylist:
       if key.strip() in nams:
             for i in range(len(list(d1[key]))):
                    idlist4.append(list(d1[key])[i])


idlist5=set(idlist3)-set(idlist4)

for i in range(len(idlist5)):
       print "%s"  % list(idlist5)[i]
