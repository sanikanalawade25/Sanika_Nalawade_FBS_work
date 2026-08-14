# Q2.Write program to calculate the sum of following series where n is input b users
# 1/1!+2/2!+3/3!..N/N!
n=int(input("Enter n:"))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(i/fact)
print('Sum of Series:',sum)
