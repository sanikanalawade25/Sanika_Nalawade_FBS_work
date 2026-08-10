# Q1. python program to put even and odd element of a list into two different lists.
li = [2, 4, 7, 12, 16, 19]

even = []
odd = []

for i in range(0, len(li)):
    if li[i] % 2 == 0:
        even.append(li[i])
    else:
        odd.append(li[i])

print('Original list:', li)
print('Even list:', even)
print('Odd list:', odd)