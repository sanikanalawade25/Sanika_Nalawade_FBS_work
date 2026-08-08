#...4write a program to find sum of n number using recusion
def son(n):
    if(n>0):
        return n+son(n-1)
    else:
        return 0
n=int(input("Enter Number:"))
res=son(n)
print(res)