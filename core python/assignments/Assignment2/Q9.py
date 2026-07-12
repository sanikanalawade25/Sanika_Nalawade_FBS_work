# Write a program to swap two numbers without using third variable.
#take number'
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
#perfrom operation
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f'After swapping num1  is:{num1} and num2 is :{num2}')