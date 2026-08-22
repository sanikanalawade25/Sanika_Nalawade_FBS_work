Subject1=int(input("Enter S1 :"))
Subject2=int(input("Enter S2 :"))
Subject3=int(input("Enter S3 :"))
Subject4=int(input("Enter S4 :"))
Subject5=int(input("Enter S5 :"))
Sum=(Subject1+Subject2+Subject3+Subject4+Subject5)
Percentage=Sum/500*100
print(Percentage)
if(Percentage>=85):
    print("First Class")
elif(Percentage>=65):
    print("Second Class")
elif(Percentage>=35):
    print("Third Class")
else:
    print("Fail")
