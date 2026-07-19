# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 
S1=int(input("Enter Subject 1 Marks:"))
S2=int(input("Enter Subject 2 Marks:"))
S3=int(input("Enter Subject 3 Marks:"))
S4=int(input("Enter Subject 4 Marks:"))
S5=int(input("Enter Subject 5 Marks:"))
Total=S1+S2+S3+S4+S5
Percentage=Total/500*100
if(Percentage>=60):
    print("First_Class")
elif(Percentage>=50):
    print("Second_Class")
elif(Percentage>=40):
    print("Pass")
else:
    print("Fail")