# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.
numbers=[4,3,2,1,6,5]
target=10
print('List',numbers)
print('target',target)
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if numbers[i]+numbers[j]+numbers[k]==target:
                print(numbers[i],numbers[j],numbers[k])