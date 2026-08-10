# Q2.Write a program find maximum and miniminum element in a list
li=[20,40,10,15]
max=li[0]
min=li[0]
for num in li:
    if num>max:
        max=num
    if num<min:
        min=num
print('Maximum',max)
print('Minimum',min)