# calculate the cost of painting th following buliding wall(both interior and exterior) you
# need to accept area (one wall )and cost of both interior and exterir wall
area=int(input("Enter area of one val 1:"))
ec=int(input("Enter cost of exterior wall"))
ic=int(input("Enter cost of interor wall"))
ex_area=area*2
ic_area=area*2
ex_cost=ex_area*ec
ic_cost=ic_area*ic
print("Exterior of Wall",ex_cost)
print("Interor of Wall",ic_cost)

print("total",ex_cost+ic_cost)


