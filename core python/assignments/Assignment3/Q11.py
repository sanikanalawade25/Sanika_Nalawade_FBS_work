# 11. Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 
age=int(input("Enter age "))
TK1=int(input("Enter Ticket_price"))
Total=0
if(age<12):
    Total=Total+(TK1-TK1*0.3)
elif(age>59):
    Total=Total+(TK1-TK1*0.5)
else:
    Total=Total+TK1

age=int(input("Enter age "))
TK2=int(input("Enter Ticket_price"))
if(age<12):
    Total=Total+(TK2-TK2*0.3)
elif(age>59):
    Total=Total+(TK2-TK2*0.5)
else:
    Total=Total+TK2

age=int(input("Enter age "))
TK3=int(input("Enter Ticket_price"))
if(age<12):
    Total=Total+(TK3-TK3*0.3)
elif(age>59):
    Total=Total+(TK3-TK3*0.5)
else:
    Total=Total+TK3

age=int(input("Enter age "))
TK4=int(input("Enter Ticket_price"))
if(age<12):
    Total=Total+(TK4-TK4*0.3)
elif(age>59):
    Total=Total+(TK4-TK4*0.5)
else:
    Total=Total+TK4
    
age=int(input("Enter age "))
TK5=int(input("Enter Ticket_price"))
if(age<12):
    Total=Total+(TK5-TK5*0.3)
elif(age>59):
    Total=Total+(TK5-TK5*0.5)
else:
    Total=Total+TK5
print('Total Price :', Total)  
