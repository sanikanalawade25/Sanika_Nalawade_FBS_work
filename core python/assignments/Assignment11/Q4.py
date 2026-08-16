# Q4. Python Program to Find the Second Largest Number in a List Using Bubble sort.

li = [12, 22, 9, 57, 1, 51, 8]

for i in range(1,len(li)):
    for j in range(0, len(li) - i ):
        if li[j] > li[j + 1]:
            li[j],li[j+1] = li[j+1],li[j]

print("Sorted list:", li)
print("Second largest number:", li[-2])