# Q1.python program to replace all occurrences of'  ' with $ in string
# Without method
s=input("Enter String")
new=''
for i in s:
    if(i=='a'):
        new=new+ '$'
    else:
        new=new+i
print('original string',s)
print('New String',new)


# with method-

# str=input('Enter String:')
# res=(str.replace('a','$'))
# print('Original String',str) 
# print('Updated String',res)