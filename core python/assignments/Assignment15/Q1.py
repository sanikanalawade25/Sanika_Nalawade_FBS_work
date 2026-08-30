#Que1. Create a class Book with members as bid,bname,price and author.
# Add following methods-
# a)constructor (support both parameterized and parameterless)
# b)destructor
# c)showBook

class Book:
    def __init__(self,id=0,name="",author="",price=""):
        self.id=id
        self.name=name
        self.author=author
        self.price=price
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def getauthor(self):
        return self.author
    def setauthor(self,newauthor):
        self.author=newauthor
    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice
    

    def showBook(self):
        print(f"id={self.id}\t name={self.name}\t Author={self.author}\t Price={self.price}")

    def __del__(self):
        print('Book Object Destroyed')

#Parameterized
book1=Book(101,'Wings of Fire','A.P.J Abdul Kalam',250)
book1.showBook()
#Parameterless
book2=Book()
book2.showBook()



