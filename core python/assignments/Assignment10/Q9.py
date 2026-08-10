# Q9 WAP to having number of element in list and find on even and odd element in that list and create two separate list which will have even element and other will have add element
n=int(input("Enter number of element in list:"))
li=[]
for i in range(0,n):
    num=int(input("Enter Number:"))
    li=li+[num]
    even=[]
    odd=[]
    for j in range(0,len(li)):
        if(li[j]%2==0):
            even=even+[li[j]]
        else:
            odd=odd+[li[j]]
print("original list ",li)
print("even list",even)
print("odd list",odd)
