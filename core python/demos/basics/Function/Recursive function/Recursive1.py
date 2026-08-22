def sOs(n):
    if(n>0):
        return n + sOs(n-1)
    else:
        return 0
n=5
res=sOs(n)
print(res)
        