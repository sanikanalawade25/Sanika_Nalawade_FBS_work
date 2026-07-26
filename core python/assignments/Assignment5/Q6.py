# 6. Write a program to print first n prime numbers.
n=int(input('Enter Number:'))
count=0 
num=2
print(f'first{n} prime number')
while(count<n):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
        count=count+1
    num=num+1
             
       