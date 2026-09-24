try:
    no1=int(input("Enter Number1:"))
    no2=int(input("Enter Number2:"))
    print(no1//no2)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:    #Specilzation
    print("Enter proper Value")
except Exception as e:
    print("Can not Divide by zero")  #Generelization
else:
    print("Not Exeception")
finally:
    print("I am from finally")
