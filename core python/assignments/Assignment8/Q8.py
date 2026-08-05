# Write program to find reverse number
def reverseNumber(n):
    rev=0
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input("Enter Number:"))
res=reverseNumber(n)
print(res)

