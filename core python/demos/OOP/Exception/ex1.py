def add():
    try:
        a=int(input("Enter Number"))
        return a
    except Exception as e:
        print(e)
        return
    finally:
        print("I am form Finally")
res=add()
print(res)