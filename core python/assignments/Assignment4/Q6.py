# 6. WAP to check if a given number is prime number or not.
n=int(input('Enter Number :'))
if(n>1):
    for i in range (2,n//2+1):
        if(n%1==0):
            print(f'{n} number is not prime')
            break
        else:
            print(f'{n} number is prime')
else:
    print(f'number is not prime or not composite')