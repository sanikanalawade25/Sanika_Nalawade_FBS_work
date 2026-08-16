s=input("Enter String:")
new=''
for i in s:
    if(i==' '):
        new=new+'-'
    else:
        new=new+i
print("Original string",s)
print('New String',new)