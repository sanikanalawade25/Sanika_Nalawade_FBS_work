from MyExeceptionUser import MyExeceptionUser
try:
    no1=int(input("Enter Number 1:"))
    no2=int(input("Enter Number 2:"))
    if(no2<=0):
        raise MyExeceptionUser()
    else:
        print(no1//no2)
except MyExeceptionUser as v:
    print(v)

except Exception as e:
    print(e)
        