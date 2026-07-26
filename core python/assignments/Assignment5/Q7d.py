# 7. Write a program to solve the following series :
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a=int(input("Enter a:"))
sum=0
for i in range(1,11):
    sum=sum+(a**i)/i
print("The Sum of series",sum)