def greet():
    num=int(input("Enter Strong Number:"))
    temp=num
    sum=0
    while(temp>0):
        d=(temp%10)
        fact=1
        for i in range(1,d+1):
            fact=fact*i
        sum=sum+fact
        temp=temp//10
    if(num==sum):
        print(f'{num} is Strong Number')
    else: 
        print(f'{num} is not strong Number')       
greet()