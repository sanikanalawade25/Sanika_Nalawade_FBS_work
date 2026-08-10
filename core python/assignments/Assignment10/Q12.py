# Q12 Write progrm to create three lists of number there square and cubes
li=[1,2,3,4,5]
square=[]
cube=[]
for i in range(0,len(li)):
    square=square+[li[i]**2]
    cube=cube+[li[i]**3]
print("original list",li)
print("square list ",square)
print("cube list",cube)