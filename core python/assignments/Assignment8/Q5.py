def sum_prime(n):
    sum=0
    for num in range(2,n+1):
        if (num>1):
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                sum=sum+num
    return sum
n=int(input("Enter Number:"))
res=sum_prime(n)
print(res)
# def sum_prime(n):
#     count=0
#     num=2
#     while(count<n):
#         for i in range(2,num):
#             if(num%i==0):
#                 break
#         else:
#             count+=1
#         num=num+1
#     return num-1
# n=int(input("Enter Number:"))
# res=sum_prime(n)
# print(res)