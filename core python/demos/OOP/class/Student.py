class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def getage(self):
        return self.age
    def setage(self,newage):
        self.age=newage
    def display(self):
        print(f"ID{self.id} Name{self.name} Age{self.age}")

Student1=Student(101,'Sanika',21)
print(Student1.getage())
Student1.setage('22')
print(Student1.getage())

 
