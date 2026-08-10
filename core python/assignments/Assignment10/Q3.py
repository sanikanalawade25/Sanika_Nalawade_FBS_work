#Q3 write program find second largest element in list
li=[13,9,25,30,35]
max=li[0]
second_max=li[0]
for num in range(1,len(li)):
    if(li[num]>max):
        second_max=max
        max=li[num]
    elif(li[num]>second_max):
        second_max=li[num]
print('maximum element',max)
print('second_maximum element',second_max)