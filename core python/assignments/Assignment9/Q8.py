def prime(num,i):
    if(num==1):
        return True
    if(num%i==0):
        return False
    return(num,i+1)
num=int(input("Enter Number:"))
if(num>1):
    res=prime(num,2)
    if res:
        print("Number Prime")
    else:
        print("Number is  Not Prime")
else:
    print("Number is Not Prime")