class Student:
    def __init__(self,rollno,name):
        self.__rollno=rollno
        self.__name=name
    def __str__(self):
        return f"RollNo={self.__rollno}\tName={self.__name}"
s1=Student(11,'Sanika')
print(s1.__rollno)# it show error because it private
        