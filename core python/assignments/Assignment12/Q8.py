# Q8.Python Program Remove Charaters odd index values in String
s=input("Enter String:")
new=''
for i in range(0,len(s)):
    if(i%2==0):
        new=new+s[i]
print("Original String",s)
print("New String",new)