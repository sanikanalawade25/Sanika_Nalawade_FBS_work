from Emp import Emp
class Hr(Emp):
    def __init__(self,id,name,sal,Comission):
        super().__init__(id, name, sal)  #Inheritance
        self.Comission=Comission
    def getComission(self):
        return self.Comission
    def setComission(self,newComission):
        self.Comission=newComission
    def calSal(self):                    #Polimorphism used
        return self.Comission+self.sal
    def display(self):
        super().display()
        print(f"Bonous{self.Comission}")
        print(f"Total Salary={self.calSal()}")
