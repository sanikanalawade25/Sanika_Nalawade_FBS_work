# Q15. python program to find largerr string without using buit in function
# Without method-
s1=input("Enter String 1:")
s2=input("Enter String 2:")
count1=0
count2=0
for i in s1:
    count1=count1+1
for i in s2:
    count2=count2+1
if(count1>count2):
    print('larger number',s1)
elif(count2>count1):
    print('larger number',s2)
else:
    print('Both Number largest')

# with method-
# n=int(input("Enter Number String:"))
# larger=''
# for i in range(n):
#     s=input("Enter String:")
#     count=0
#     for i in s:
#         count=count+1
#         larger_count=0
#     for j in larger:
#         larger_count=larger_count+1
#     if(count>larger_count):
#         larger=s
# print("larger string",larger)