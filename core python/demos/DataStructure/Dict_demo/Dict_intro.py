# 1.key(custimized indexing)&value pair
di={1:'python','Relesed':1991,'Developer':'Guido Van Rossum',}

#2 hetoregenous

# 3ordered

# 4key:Immutable,value:Mutable,dict:Size-mutable
# di[1]='Python Programming'
# print(type(di))
# print(di)
#
# 5.key unique , values:Duplicate allowed
di[1]='Java' # key value are replace [1]=python replce is [1] Java
di[3]=100 # key [3] is not existing than it add last in dict
print(type(di))
print(di)
