#Que2. Create a class Product with members as id,name,price and quantity.
# Add following methods-
# a)constructor (support both parameterized and parameterless)
# b)destructor
# c)showBook

class Product:
    def __init__(self,id="",name="",price="",quantity=0):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice
    def getauthor(self):
        return self.quantity
    def setauthor(self,quantity):
        self.quantity=quantity
    

    def showProduct(self):
        print(f"id={self.id}\t name={self.name}\t Price={self.price}\t Quantity={self.quantity}")

    def __del__(self):
        print('Product Object Destroyed')

#Parameterized
product=Product(101,'Mobile',100000,1)
product.showProduct()
#Parameterless
product2=Product()
product2.showProduct()



