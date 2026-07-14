# WAP to calculate selling price of book based on cost price and discount.
#take input

cost_price=int(input("Enter cost price:"))
discount=int(input("Enter discount :"))
# perfrom operation
selling_price = cost_price - discount 
print(f'Selling price of book is:{selling_price}')