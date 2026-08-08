def power(m,n):
    if(n>0):
        return m*power(m,n-1)
    else:
        return 1
m=int(input("Enter Number m :"))
n=int(input("Enter Number n :"))
res=power(m,n)
print(f'power of{m} is {n}={res}')