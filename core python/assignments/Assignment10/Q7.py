# Q7 WAP to crete new list from existing list which contains cube of each number of list
li=[2,3,4,5]
new=[]
for i in li:
    cube=i**3
    new=new+[cube]
print("original list",li)
print("new",new)