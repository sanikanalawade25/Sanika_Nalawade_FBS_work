# Q1 A list contains denominations as follows:
#D=[2000,500,200,100,50,20,10,5]
#Accept amount from user and calculate how man minimum number will be noted ofnotes will nedded from thant amount
D=[2000,500,200,100,50,20,10,5]
amt=int(input("Enter Amount:"))
count=0
for note in D:
    count=count+(amt//note)
    amt=amt%note
print("Mimiumum number of notes:",count)
