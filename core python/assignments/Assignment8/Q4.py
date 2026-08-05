def  odd(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n = int(input("Enter Number :"))
res=odd(n)
print(res)