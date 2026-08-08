# Q10 wite program to reverse number using recursion
def reverseNumber(n,rev):
    if(n>0):
        d=n%10
        rev=rev*10+d
        return reverseNumber(n//10,rev)
    else:
        return rev
n=int(input("Enter Number:"))
res=reverseNumber(n,0)
print(res)