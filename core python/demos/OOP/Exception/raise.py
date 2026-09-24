try:
    no1=int(input("Enter Number 1:"))
    no2=int(input("Enter Number 2:"))
    if(no2<=0):
        raise Exception("Number not print proper")
    else:
        print(no1//no2)
except Exception as e:
    print(e)
        