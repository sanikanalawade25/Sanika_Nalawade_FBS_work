# 6. Write a program to calculate profit or loss.
selling_price=int(input("Enter Selling_price:"))
cost_price=int(input("Enter cost_price:"))
if(selling_price>cost_price):
    print('Profit')
elif(selling_price<cost_price):
    print('loss')
else:
    print('No profit and No loss')