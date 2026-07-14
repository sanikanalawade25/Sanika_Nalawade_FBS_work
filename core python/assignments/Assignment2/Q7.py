# Find the sum of three-digit number.
# take input
num=int(input("Enter three digit number:"))
temp=num
#perfrom operation
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10
sum=d1+d2+d3
print(f'The sum of{temp} is {sum}:')