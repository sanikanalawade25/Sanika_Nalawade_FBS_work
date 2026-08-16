# Q10.Python Program to  take in take in two string an display the larger string without using built in function
s1=input("Enter String 1:")
s2=input("Enter String 2:")
l1=0
l2=0
for i in s1:
    l1=l1+1
for i in s2:
    l2=l2+1
if(l1>l2):
    print('Largest String ',s1)
elif(l2>l1):
    print('Largest String',s2)
else:
    print('Both string Largest')