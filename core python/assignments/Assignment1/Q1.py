#Write a program to calculate the percentage of student based on marks of any 5 subjects.

#Take 5 Subjects Marks

Subjects=int(input("Enter Number of Subjects:"))
Subject1=int(input("Enter Subject 1 Marks:"))
Subject2=int(input("Enter Subject 2 Marks:"))
Subject3=int(input("Enter Subject 3 Marks:"))
Subject4=int(input("Enter Subject 4 Marks:"))
Subject5=int(input("Enter Subject 5 Marks:"))

Total=Subject1+Subject2+Subject3+Subject4+Subject5
Percentage=(Total/500)*100

print(f'Percentage: {Percentage}')