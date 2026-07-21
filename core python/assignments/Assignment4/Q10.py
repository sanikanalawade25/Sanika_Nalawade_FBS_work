# 10. WAP to check if given number is Perfect Number.
num=int(input('Enter Number :'))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print('The Number is Perfect')
else:
    print('The Number is Not Perfect')
