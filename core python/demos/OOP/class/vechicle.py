class Vechicle:
    def __init__(self,id,brand,model):
        self.id=id
        self.brand=brand
        self.model=model
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getbrand(self):
        return self.brand
    def setbrand(self,newbrand):
        self.brand=newbrand
    def getmodel(self):
        return self.model
    def setmodel(self,newmodel):
        self.model=newmodel
    def display(self):
        print(f"Id{self.id} Name{self.brand} Model{self.model}")

Vechicle1=Vechicle(101,'Toyota','Hyrider')
print(Vechicle1.getmodel())
Vechicle1.setmodel('Hybrid')
print(Vechicle1.getmodel())


