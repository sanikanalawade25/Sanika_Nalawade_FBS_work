from Hr import Hr
from developer import Developer
class EmployeeManagement:
    def __init__(self):
        self.edetils={}
    def addEmp(self):
       empid=int(input("Enter the Id of Emp"))
       if empid in self.edetils:
            print("Emp Alredy Exist")
            return
       else:
            name=input("Enter the Name of Emp")
            sal=float(input("Enter the Sal of Emp"))
            print("1.Hr")
            print("2.Developer")
            choice=int(input("Enter your choice="))
            if choice==1:
                com=float(input("Enter the com of Hr="))
                emp=Hr(empid,name,sal,com)
            elif choice==2:
                Bonous=float(input("Enter the Bonous of Developer ="))
                emp=Developer(empid,name,sal,Bonous)
            else:
                print("Invalid choice...")
                return
            self.edetils[empid]=emp
            print("Emp added Suceefully...")


    def DisplayEmp(self):
        if len(self.edetils)==0:
            print("Employye not Exist....")
        else:
            for emp,empobj in self.edetils.items():
                print(emp,empobj)

    def SearchEmp(self):
        if len(self.edetils)==0:
            print("Employee not Exist...")
        else:
            eid=int(input("Enter the Id of Employee "))
            if eid in self.edetils:
                print("EmpDetils=",self.edetils[eid])
            else:
                print(f"Employee with {eid} is not present")
    def UpdateEmp(self):
    
        if len(self.edetils) == 0:
            print("Employee not Exist....")

        else:
            eid = int(input("Enter the Id of Employee to Update: "))

            if eid in self.edetils:

                emp = self.edetils[eid]

                print("Current Employee Details:")
                print(emp)

                name = input("Enter new Name: ")
                sal = input("Enter new Salary: ")

                if name != "":
                    emp.name = name

                if sal != "":
                    emp.sal = float(sal)

                if isinstance(emp, Hr):
                    com = input("Enter new Commission: ")

                    if com != "":
                        emp.com = float(com)

                elif isinstance(emp, Developer):
                    bonus = input("Enter new Bonus: ")

                    if bonus != "":
                        emp.Bonous = float(bonus)

                print("Employee Updated Successfully...")
                print("Updated Details:")
                print(emp)

            else:
                print(f"Employee with {eid} is not present")

    def DeleteEmp(self):
        
    
        if len(self.edetils) == 0:
            print("Employee not Exist....")

        else:
            eid = int(input("Enter the Id of Employee to Delete: "))

            if eid in self.edetils:
                del self.edetils[eid]
                print("Employee Deleted Successfully...")

            else:
                print(f"Employee with {eid} is not present")
    
       