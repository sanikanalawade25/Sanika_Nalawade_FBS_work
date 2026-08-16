# Q4 Pthon Program to General Dictionar that Conatins Number (between 1 and n) in from (x,x*x)
# without method-
n=int(input('Enter n:'))
d={}
for i in range(1,n+1):
    d[i]=i*i
print('Dictionary',d)

# with method-
# n=int(input('Enter n:'))
# d={}
# for i in range(1,n+1):
#     d.update({i:i*i})
# print('Dictionary',d)