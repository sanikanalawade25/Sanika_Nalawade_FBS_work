# Q5 Accept number fro user and check if element is present in list or not also tell how  many time present in list 
li=[10,20,30,40,50,10,50]
num=int(input("Enter Number to check:"))
count=0
for i in range(0,len(li)):
    if(li[i]==num):
        count=count+1
        if(count>0):
            print("Number is present in the list")
            print("count of number",count)
        else:
            print("Number is Not present in the list")