# Q7.Python Program to remove then given from dictionary
d={'a':1,'name':'Sanika','age':21}
key=input("Enetr Remove key:")
if key in d:
    d.pop(key)
    print('Update Dictionary=',d)
else:
    print('key does not exist')