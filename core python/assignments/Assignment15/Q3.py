#Que1. Create a class Shirt with members as sid,sname,type and price size.
# Add following methods-
# a)constructor (support both parameterized and parameterless)
# b)destructor
# c)showBook

class Shirt:
    def __init__(self,id=0,name="",type="",price="",size=""):
        self.id=id
        self.name=name
        self.type=type
        self.price=price
        self.size=size
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def gettype(self):
        return self.type
    def setauthor(self,newtype):
        self.type=newtype
    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice
    def getsize(self):
        return self.size
    def setsize(self,newsize):
        self.size=newsize
    

    def showShirt(self):
        print(f"id={self.id}\t name={self.name}\t Type={self.type}\t Price={self.price}\t Size={self.size}")

    def __del__(self):
        print('Shirt Object Destroyed')

#Parameterized
s1=Shirt(101,'Siya Ram','Casual',250,'Small')
s1.showShirt()
#Parameterless
s2=Shirt()
s2.showShirt()



