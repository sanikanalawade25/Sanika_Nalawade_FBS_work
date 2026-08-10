# Q10 WAP program to remove all occurrences of given element in list

li=[10,20,30,10,20]
num=int(input("Enter number to remove:"))
new=[]
for i in range(0,len(li)):
    if(li[i]!=num):
        new=new+[li[i]]
print("original list",li)
print("new list",new)