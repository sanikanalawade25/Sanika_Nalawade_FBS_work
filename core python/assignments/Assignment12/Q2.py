# Q1.Python Program Remove nth index charater from Non- Empty String
# Without Method
str=input('Enter String:')
n=int(input('Enter n:'))
new=''
for i in range(0,len(str)):
    if(i!=n):
        new=new+str[i]
print('Original String',str)
print('new  string',new)
 
# with method 

# str=input('Enter String:')
# n=int(input('Enter index:'))
# new=str[:n]+str[n+1:]
# print('new string',new)
