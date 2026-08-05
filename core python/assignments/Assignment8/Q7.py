def sod(n):
    sum=0
    while(n>0):
        d=n%10
        n=n//10
        sum=sum+d
    return sum
n=int(input('Enter Number:'))
res=sod(n)
print(res)
    