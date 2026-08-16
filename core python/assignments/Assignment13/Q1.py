# Q1 Python Program To add ke value pair to the dictionar
# d={'id':1,'name':'Sanika','Age':21}
# key=input("Enter key:")
# value=input("Enter Value:")
# d[key]=value
# print('Updated dictionary',d)

d={'id':1,'name':'Sanika','Age':21}
key=input("Enter key:")
value=input("Enter Value:")
d.update({key :value})
print('Updated dictionary',d)