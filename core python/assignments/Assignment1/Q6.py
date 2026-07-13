# Write a Program to input two angles from user and find third angle of the triangle
#Take input
angle1=int(input("Enter Angle 1:"))
angle2=int(input("Enter Angle 2:"))
#Find third angle
angle3=180-(angle1+angle2)
print(f'Third Angle is: {angle3}')