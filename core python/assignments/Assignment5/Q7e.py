# 7. Write a program to solve the following series :
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x=int(input("Enter Number:"))
n=int(input("Enter ending number:"))
dem=1
sign=1
sum=0
for i in range(1,n+1):
    sum+=(sign*(x**i)/dem)
    dem+=2
    sign*=-1
print(f'The sum of series:{sum}')