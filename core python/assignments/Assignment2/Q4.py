# WAP to calculate area of triangle and rectangle
#take input
base=int(input("Enter base:"))
height=int(input("Enter height:"))
#calculat area of triangle
Area_triangle=(base*height)/2

# take input for rectangle
length=int(input("Enter length:"))
breadth=int(input("Enter breadth:"))
# calculate area of rectangle
Area_rectangle=length*breadth
# display results
print(f'Area of triangle: {Area_triangle}')
print(f'Area of rectangle: {Area_rectangle}')