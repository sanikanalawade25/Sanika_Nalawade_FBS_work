# Q4 Write Python Program That finds all pairs of element in list whose sum is equal
li=[1,2,3,4,5,6,7,8,9]
target=int(input('Enter Target element:'))
pair=set()
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i]+li[j]==target):
            pair.add((li[i],li[j]))
print('list',li)
print('Target',target)
print('Pairs',pair)