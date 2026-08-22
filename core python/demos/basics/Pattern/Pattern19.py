for i in range(1,6):
    for  j in range(1,6-i):
        print(' ',end=' ')
    for j in range(6-i,6):
        if(i==j or i+j==6 or i+j==8):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()