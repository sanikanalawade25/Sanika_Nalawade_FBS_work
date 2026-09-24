# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:
    def __init__(self,id,name,age,percentage):
        self.id=id
        self.name=name
        self.age=age
        self.percentage=percentage

    def accept(self):
        self.id=int(input("Enter Student ID:"))
        self.name=input("Enter Student Name:")
        self.age=int(input("Enter Student Age:"))
        self.percentage=float(input("Enter Student Perecentage:"))

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
    def getpercentage(self):
        return self.percentage
    def setpercentage(self,newpercentage):
        self.percentage=newpercentage

    def display(self):
        print(f"ID={self.id} Name={self.name} Age={self.age} Percentage={self.percentage}\nRank:{self.CalculateRank()}")

    def CalculateRank(self):
        if self.percentage>=75:
            return "Distinction"
        elif self.percentage>=60:
            return "First Class"
        elif self.percentage>=45:
            return "Second Class"
        elif self.percentage>=35:
            return "Third Class"
        else:
            return "Fail"
    def __str__(self):
        return f"ID:{self.id}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.percentage}"
    
       
class EnggStudent(Student):
    def __init__(self, id, name, age, percentage, branch, internal_marks):
        super().__init__(id, name, age, percentage)
        self.branch=branch
        self.internal_marks=internal_marks

    
    def accept(self):
        super().accept()
        self.branch=input("Enter Branch:")
        self.internal_marks=float(input("Enter Internal Marks:"))

    def display(self):
        super().display()
        print(f"Branch:{self.branch}\nInternal Marks:{self.internal_marks}")

    def CalculateRank(self):
        super().CalculateRank()

    def __str__(self):
        return f"{super().__str__()}\nBranch:{self.branch}\nInternal Marks:{self.internal_marks}"

e1=EnggStudent(101,"Sanika",18,75,"CS",89)
e1.display()
print(e1)

e2=EnggStudent(0,"",0,0,"",0)
e2.accept()