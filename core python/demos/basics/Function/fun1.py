def greet():
    num=int(input("Enter Number:"))
    temp=num
    rev=0
    while(num>0):
        d=num%10
        num=num//10
        rev=rev*10+d
    if(temp==rev):
        print('palindrome')
    else:
        print('Not palindrome')
greet()