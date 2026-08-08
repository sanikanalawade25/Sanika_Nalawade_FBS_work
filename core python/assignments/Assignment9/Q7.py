#...7write a program to find sum of digits using recursion 
def sod(n):
    if(n>0):
        d=n%10
        n=n//10
        return d+sod(n)
    else:
        return 0
n=int(input('Enter Number:'))
res=sod(n)
print('Sum of digit:',res)