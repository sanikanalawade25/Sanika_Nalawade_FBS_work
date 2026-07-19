# Write a program to input all sides of a triangle and check whether triangle is valid or not
FS=int(input("Enter FS:"))
SS=int(input("Enter SS:"))
TS=int(input("Enter TS:"))
if(FS+SS>TS and SS+TS>FS and TS+FS>SS):
    print("Triangle is Valid")
else:
    print("Trianle is not Valid")