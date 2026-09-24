class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def getsal(self):
        return self.sal
    def setsal(self,newsal):
        self.sal=newsal

    def calSal(self):
        print(f"I am From Emp")
#End With Employeee
class Hr(Emp):
    def __init__(self,id,name,sal,Comission):
        super().__init__(id, name, sal)  #Inheritance
        self.Comission=Comission
    def getComission(self):
        return self.Comission
    def setComission(self,newComission):
        self.Comission=newComission
    def calSal(self):
        print(f"I am From Hr salary")
#End with Hr
class developer(Emp):
    def __init__(self, id, name, sal,Bonous):
        super().__init__(id, name, sal)
        self.Bonous=Bonous
    def getBonous(self):
        return self.Bonous
    def setBonous(self,newBonous):
        self.Bonous=newBonous 
    def calSal(self):
        print(f"I am From Developer Sal")      
#End With deveplor
Emp1=Emp(16,'Sanika',45000)
Emp2=Hr(13,'Sai',200000,3000)
Emp3=developer(12,'Sahil',200100,30)
Emp1.calSal()
Emp2.calSal()
Emp3.calSal()


    
        

# e1=Emp(101,'Sanika',50000)
# # e1.disply()
# print(e1.getname())
# e1.setname('sai')
# print(e1.getname())
    
        
        
        