from abc import ABC,abstractmethod #Abstraction used
class Emp(ABC):
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
    @abstractmethod        #Absrtaction is used
    def calSal(self):
        pass
    def __str__(self):
        return f"id={self.id}\t name={self.name}\t sal={self.sal}"

      







    
        

# e1=Emp(101,'Sanika',50000)
# # e1.disply()
# print(e1.getname())
# e1.setname('sai')
# print(e1.getname())
    
        
        
        
        
        