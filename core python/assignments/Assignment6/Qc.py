# Q3 write program to print following patterns
for i in range(1,5):
    k=1
    for j in range(1,5-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(' ',k,end=' ')
        k=k*(i-j)//j
    print()