# Q1.Write program to print first n prime number
n=int(input("Enter Prime Number:"))
count=0
num=2
print(f'First {n}prime number')
while(count<n):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
        count=count+1
    num=num+1

       