#Q6. Python Program Take String And replace every Blank with Hypen
s=input("Enter String:")
new=''
for i in s:
    if(i==' '):
        new=new+'-'
    else:
        new=new+i
print('Original string',s)
print('New string ',new)
        