# Q5 write program to print following patterns
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(6-i,6):
        print('*',end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print()