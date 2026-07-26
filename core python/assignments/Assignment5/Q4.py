# 4. WAP to print Armstrong number within a given range
start=int(input("Enter start Number:"))
end=int(input("Enter end Number:"))
for num in range(start,end+1):
    count=len(str(num))
    temp=num
    total=0
    while(num>0):
        d=num%10
        total=total+(d**count)
        num=num//10
    if(total==temp):
        print(temp)