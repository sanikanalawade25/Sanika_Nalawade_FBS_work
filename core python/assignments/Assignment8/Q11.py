#Q11 WAP to check if given number ArmStrong Number or not for each task create separate  function
def armStrong(n):
    count=len(str(n))
    temp=n
    total=0
    while(n>0):
        d=n%10
        total=total+(d** count)
        n=n//10
    if total==temp:
        return True
    else:
        return False
n=int(input("Enter Number:"))
res=armStrong(n)
print(res)