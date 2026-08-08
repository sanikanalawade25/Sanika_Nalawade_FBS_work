def son(n):
    if(n>0):
        return n+son(n-1)
    else:
        return 0
n=int(input("Enter Number:"))
res=son(n)
print(res)