# Write a program to enter P, T, R and calculate Compound Interest.
#Take Input
P=int(input("Enter Principal Amount :"))
T=int(input("Enter Time :"))
R=int(input("Enter Rate of Interest :"))
#perfrom operation
Amount=P*(1+R/100)**T
# Caluclate Compound Interest
CI=Amount-P

print('Compound Interest:',CI)