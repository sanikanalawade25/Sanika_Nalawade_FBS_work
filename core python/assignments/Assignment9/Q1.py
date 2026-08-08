# Q1.Write 
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
