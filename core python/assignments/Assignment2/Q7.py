# Find the sum of three-digit number.
# take input
num=int(input("Enter three digit number:"))
#perfrom operation
first_digit=num//100
second_digit=(num//10)%10
third_digit=num%10
sum=first_digit+second_digit+third_digit
print(f'sum of three digit number is :{sum}and first digit is:{first_digit} and second digit is :{second_digit} and third digit is:{third_digit}')