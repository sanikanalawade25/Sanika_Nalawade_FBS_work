# Q2. Python program to concatenate two dictionaries into one
# Without method-
d1={'a':10,'b':20}
d2={'c':30,'d':40}
d={}
for key in d1:
    d[key]=d1[key]
for key in d2:
    d[key]=d2[key]
print('dictionary d1',d1)
print('dictionary d2',d2)
print('concatenate dictionary',d)

# With method
# d1={'a':10,'b':20}
# d2={'c':30,'d':40}
# print('dictionary d1',d1)
# d1.update(d2)
# print('dictionary d2',d2)
# print('concatenate dictionary',d1)

