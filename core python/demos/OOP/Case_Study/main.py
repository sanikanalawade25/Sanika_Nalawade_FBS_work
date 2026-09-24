from Empmanagment import EmployeeManagement
class Login:
    def login():
        emg=EmployeeManagement()
        userid='admin'
        password='1234'
        uname=input("Enter username:")
        passw=input("Enter password:")
        if uname==userid and passw==password:
            print("\nLogin successful")
            while True:
                print("Enter 1 for Add Emp")
                print("Enter 2 for Display Emp ")
                print("Enter 3 for Serach Emp")
                print("Enter 4 for Updated Emp")
                print("Enter 5 for Delete Emp")
                print("Enter 6 for Exist")
                ch=int(input('Enter the choice:'))
                if ch==1:
                    emg.addEmp()
                elif ch==2:
                    emg.DisplayEmp()
                elif ch==3:
                    emg.SearchEmp()
                elif ch==4:
                    emg.UpdateEmp()
                elif ch==5:
                    emg.DeleteEmp()
                elif ch==6:
                    print('Thank you')
                    break
        else:
            
            print("Invalid Username and Password")
Login.login()
