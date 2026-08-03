# Q2 write program to print following patterns


for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

for i in range(1,6):
    for i in range(1,6-i):
        print('*',end=' ')
    print()