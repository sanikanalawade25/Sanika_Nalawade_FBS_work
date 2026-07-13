# Write a program to enter P, T, R and calculate simple Interest.

#take input 
P=int(input("Enter Principal Amount :"))
T=int(input("Enter Time :"))
R=int(input("Enter Rate of Interst :"))
#perfrom operation
SI=(P*T*R)/100
# print(SI)
print('Simple Interest:',SI)