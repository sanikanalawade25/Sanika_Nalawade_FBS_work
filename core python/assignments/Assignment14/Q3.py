# Q3.Write pthon Program to find all the unquie Words and count frequency of occuerrence from given list of string use python set data type
li=['Satara','Wai','Satara','Wai','Pune','Satara']
s=set(li)
print('list',li)
print('Unique word',s)
for word in s:
    count=li.count(word)
    print(word,'=',count)