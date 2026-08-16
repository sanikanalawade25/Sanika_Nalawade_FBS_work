# Q5 python program to count Number Vowels String

s=input('Enter String:')
count=0
for i in s:
    if i in 'aeiouAEIOU':
        count+=1
print('Number of Vowels',count)