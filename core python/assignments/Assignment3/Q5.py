# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
FS=int(input("Enter FS:"))
SS=int(input("Enter SS:"))
TS=int(input("Enter TS:"))
if(FS==SS==TS):
    print("Triangle is Equilateral")
elif(FS==SS or SS==TS or TS==FS):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")