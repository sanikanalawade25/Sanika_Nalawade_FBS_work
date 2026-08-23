# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
s1={10,20,30,40,50}
s2={20,40,60,70,80}
print('set s1',s1)
print('set s2',s2)
missing_in_s2=s1.difference(s2)
missing_in_s1=s2.difference(s1)
print('missing in s2',missing_in_s2)
print('missing in s1',missing_in_s1)




