# Q3.Python Program to check if given keyy exists in dictionary or not
# Withot method
d={'id':101,'name':'sanika','city':'satara'}
key=input("Enter serach key:")
if(key in d):
    print('key Alredy exist')
else:
    print('key does not in dictionary')

# With method-
# d={'id':101,'name':'sanika','city':'satara'}
# key=input("Enter serach key:")
# if(d.get(key)!=None):
#     print('key alredy exist')
# else:
#     print('key does not in dictionary')


