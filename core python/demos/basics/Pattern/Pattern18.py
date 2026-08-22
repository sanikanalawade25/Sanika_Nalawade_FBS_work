for i in range(1,6):
    for j in range(1,6-i):
        print(' ', end=' ')
    for j in range(6-i,6):
        if(i+j==6 or i+j==8 or i+j==10):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,i):
        if(i+j==3 or i+j==7 or i+j==5 or i+j==9):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
