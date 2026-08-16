# Q.6 Python Prorgrm to multiply All the items in dictionary
# d={'a':2,'b':3,'c':4,'d':5}
# mul=1
# for i in d:
#     mul=mul*d[i]
# print('Dictionary',d)
# print('Multiply All items in dictionary',mul)

d={'a':2,'b':3,'c':4,'d':5}
mul=1
for i in d.values():
    mul=mul*i
print('Dictionary',d)
print('Multiply All items in dictionary',mul)