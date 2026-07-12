# Convert distant given in feet and inches into meter and centimeter.
#take input
feet=int(input("Enter feet:"))
inches=int(input("Enter inches:"))
#perfrom  opertion
total_inches=(feet*12)+inches
meter=total_inches*0.0254
centimeter=total_inches*2.54
print(f'distance in meter:{meter} and distance in centemeter:{centimeter}')
