# Q11 Write pogram to print all number which are divisible by m and n in the list 
li=[10,5,13,24,8,20,30]
m=int(input("Enter number m:"))
n=int(input("Enter number n:"))
print("Number divisible byy {m} and {n}")
for i in range(0,len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i])