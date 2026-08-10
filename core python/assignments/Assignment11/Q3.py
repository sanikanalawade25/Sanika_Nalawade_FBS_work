# Q3. Python Program to Sort the List According to the Second Element in Sublist.

li = [[1, 4], [4, 2], [3, 1], [6, 4]]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i][1] > li[j][1]:
            li[i],li[j] =li[j],li[i]

print("Sorted list:", li)