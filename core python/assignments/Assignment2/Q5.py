# WAP to calculate selling price of book based on cost price and discount.
#take input

cost_price=int(input("Enter cost price:"))
discount=int(input("Enter discount percentage:"))
# perfrom operation
selling_price = cost_price - (cost_price * discount / 100)
print(f'Selling price of book is:{selling_price} and cost price of book is :{cost_price}and discount percentage is :{discount}%')