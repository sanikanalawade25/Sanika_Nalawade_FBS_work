#1... Write program to find sum of following series using recursive functions:
#... 1!+2!+3!+4!+....+n!
#... Note for fact and sum two recursive functions
def fact(n):
    if(n>0):
        return n*fact(n-1)
    else:
        return 1
def sumfact(n):
    if(n>0):
        return fact(n)+sumfact(n-1)
    else:
        return 0
n=int(input("Enter Number:"))
res=sumfact(n)
print(f'sum of factorial',res)
