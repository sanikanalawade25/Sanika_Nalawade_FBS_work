# python program from new string Where the first character and the last charater have been Exchanged
# without method-
s=input('Enter String:')
new=s[len(s)-1]
for i in range(1,len(s)-1):
    new=new+s[i]
new=new+s[0]
print('original string',s)
print('new string',new)

# with method - 
   
# s=input("Enter String:")
# new=s[len(s)-1]+s[1:len(s)-1]+s[0]
# print('new string',new)
