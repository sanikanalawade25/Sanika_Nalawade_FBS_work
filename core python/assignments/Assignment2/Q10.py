# Write a program to reverse three-digit number.
#take input
num=int(input("Enter three digit number:"))
#perfrom operation
first_digit=num//100
second_digit=(num//10)%10
third_digit=num%10
reversed_num=(third_digit*100)+(second_digit*10)+first_digit
print(f'Reversed number is :{reversed_num} and first digit is:{first_digit}and second digit is  :{second_digit} and third digit is:{third_digit}')
