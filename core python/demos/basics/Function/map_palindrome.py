def chkepallindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        rev= rev*10+d
        temp//=10
    if(num==rev):
        return True
    else:
        return False
data=[121,123,8767]
res=list(map(chkepallindrome,data))
print(res)
