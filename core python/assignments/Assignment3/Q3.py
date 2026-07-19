# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.
First_angle=int(input("Enter First_angle :"))
Second_angle=int(input("Enter Second_angle :"))
Third_angle=int(input("Enter Third_angle :"))
if(First_angle+Second_angle+Third_angle==180):
    print('Triangle is valid')
else:
    print('Triangle is not valid')
