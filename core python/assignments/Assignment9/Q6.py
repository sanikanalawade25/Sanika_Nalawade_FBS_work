def fibonacci(n,a,b):
    if(n>0):
        c=a+b
        print(c,end=' ')
        return fibonacci(n-1,b,c)
n=int(input('Enter Number:'))
print("fibonacci series")
fibonacci(n,-1,1)