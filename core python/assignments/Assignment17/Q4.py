# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method
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
    
class CollageStudent:
    def __init__(self,numberofstudent):
        self.numberofstudent=numberofstudent
        self.student=[]

    def AddStudent(self,student):
        self.student.append(student)


    def GetStudent(self,id):
        for s in self.student:
            if s.id==id:
               return s
        return None

    def RemoveStudent(self,id):
        for s in self.student:
            if s.id==id:
                self.student.remove(s)
                return 

    def __str__(self):
            result=""
            for s in self.student:
                result=result+str(s)+ "\n"
            return result
c=CollageStudent(4)
s1=Student(10,'sanika',21,99)
s2=Student(20,'Sahil',23,90)
s3=Student(30,'Sai',20,65)
s4=Student(40,'Rahul',19,20)

c.AddStudent(s1)
c.AddStudent(s2)
print(c)

print(c.GetStudent(10))

c.RemoveStudent(20)
print(c)

s4.display()


        