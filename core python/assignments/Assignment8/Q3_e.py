def sos(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(n**i)
    return sum
n = int(input("Enter Number :"))
res=sos(n)
print(res)