# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.
li = ["sai", "cats", "banana", "hello", "mango"]
print("orginal list=",li)
li.sort(key=len)

print("Sorted List =", li)