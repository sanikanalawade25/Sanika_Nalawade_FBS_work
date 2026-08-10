li=[30,40,15,3,10]
new=[]
for i in range(0,len(li)):
    if(li[i]%2!=0):
        new=new+[li[i]]
print("original list",li)
print("remove even number after",new)