# Q8 WAP program to crete dupliacte of existing list is should not point to same list
li=[10,20,30,40,50]
new=[]
for i in li:
    new=new+[i]
print("original list",li)
print("duplicate list",new)
print(li is new)
