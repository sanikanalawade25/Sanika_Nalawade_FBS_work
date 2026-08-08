#2... Write a program to check if given number is ArmStron or not using recurive function
def armStrong(n):
    if(n>0):
        d=n%10
        return d**count+armStrong(n//10)
    else:
        return 0
n=int(input("Enter Number :"))
count=len(str(n))
res=armStrong(n)
if(res==n):
    print("ArmStrong Number")
else:
    print("Not ArmStrong Number ")