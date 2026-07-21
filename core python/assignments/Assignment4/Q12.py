no=int(input("Enter the Number check :"))
count= len(str(no))
temp=no
total=0
while(no>0):
    d=no%10
    total= total+(d** count)
    no=no//10
print(total)
if total==temp:
    print("number is armstrong ")
else:
    print("number is not armstrong")