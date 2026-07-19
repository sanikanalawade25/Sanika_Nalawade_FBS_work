# 12. Write a program to check if given 3 digit number is a palindrome or not. 
num=int(input("Enter Number:"))
temp=num
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10
reverse=d1*100+d2*10+d3
if(reverse==temp):
    print('Palidrome')
else:
    print('Not Palidrome')


