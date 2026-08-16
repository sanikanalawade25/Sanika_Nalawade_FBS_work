# Q12.Python Program Count Number LowerCase Charaters in string
# Without method-
s=input("Enter String:")
count=0
for i in s:
    if(i>'a'and i<'z'):
        count=count+1
print('count Number lowercase charater',count)


# With method
# s=input('Enter String:')
# count=0
# for i in s:
#     if i.islower():
#         count=count+1
# print('count Number lowercase charater',count)
 
