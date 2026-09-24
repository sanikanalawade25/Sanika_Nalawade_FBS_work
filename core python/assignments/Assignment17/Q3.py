# 3. Create a class MedicalStudent inherited from Student with following
# :
# i. Data members :Specialization
# ii. MarksOfInternship
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
    
       
class MedicalStudent(Student):
    def __init__(self, id, name, age, percentage, specilization, marksintership):
        super().__init__(id, name, age, percentage)
        self.specilization=specilization
        self.marksintership=marksintership

    
    def accept(self):
        super().accept()
        self.specilization=input("Specilization:")
        self.marksintership=float(input("Enter marksintership:"))

    def getspecilization(self):
        return self.specilization
    def setspecilization(self,newspecilization):
        self.specilization=newspecilization

    def getmarksintership(self):
        return self.marksintership
    def setmarksintership(self,newsmarksintership):
        self.marksintership=newsmarksintership
    

    def display(self):
        super().display()
        print(f"Specilization:{self.specilization}\nInternal Marks:{self.marksintership}")

    def CalculateRank(self):
        super().CalculateRank()

    def __str__(self):
        return f"{super().__str__()}\nSpecilization:{self.specilization}\nmarksintership:{self.marksintership}"
# s1=Student(10,'sanika',21,99)
# s1.display()
# print(s1.CalculateRank())
# print(s1)


# s2=Student(0,"",0,0)
# s2.accept()
# s2.display()

m1=MedicalStudent(101,"Sanika",18,75,"CS",89)
m1.display()
print(m1)

m2=MedicalStudent(0,"",0,0,"",0)
m2.accept()
        