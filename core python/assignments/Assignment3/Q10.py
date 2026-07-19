# 10. Write a program to check if person is eligible to marry or not (male age >=21 and 
# female age>=18) 
gender=input("Enter Gender(M/F):")
age=int(input("Enter Age:"))
if(gender=='F'):
    if(age>=18):
        print('eligible for marry')
    else:
        print('Not eligible for marry')
else:
    if(age>=21):
        print('eligible for marry')
    else:
        print('Not eligible for marry')