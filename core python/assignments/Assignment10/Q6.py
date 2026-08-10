# Q6 Write Program to remove duplicates   from the list
li=[10,20,10,30,40,50]
new=[]
for i in li:
    if(i not in new):
        new=new+[i]
print("Original List:",li)
print("Duplicate list",new)

