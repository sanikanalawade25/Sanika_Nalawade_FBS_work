# Write program to check if enterd palindrome number or not
def palindromeNumber(num):
    temp=num
    rev=0
    while(num>0):
        d=num%10
        num=num//10
        rev=rev*10+d
   
    if(temp==rev):
        return True
    else:
        return False
num=int(input("Enter Number:"))
res=palindromeNumber(num)
print(res)
