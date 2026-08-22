def addEmp(id,name,sal,dept):
    if(id not in all_emp_details):
        all_emp_details[id]=[id,name,sal,dept]
        return'Employee added succefully.'
    
    else:
        return'ID already exits.'
def showAllEmp():
    print(all_emp_details)#check employee id succefully

def updEmp(id):
    print("Note: If dont't want to change leave field blank.")
    emp=all_emp_details.get(id)
    if(emp):
        name=input(f'Enter New NAME({emp[1]}):'or emp[1])
        sal=int(input(f'Enter New SALARY({emp[2]}):')or 0)or emp[2]#enter string false value 0will false value all false emp[2]true =false true=true 
        dept=input(f'Enter New DEPARTMENT({emp[3]}):'or emp[3])
        all_emp_details[id]=[id,name,sal,dept]
        return 'Employee updated successfully'
    else:
        return 'ID not found.'

def deleteEmp(id):
    if id in all_emp_details:
        del all_emp_details[id]
        return'###Delete employee details Successfully###.'
    else:
        return'ID is not found.'
    
    
def searchEmp(id):
    emp=all_emp_details.get(id)
    if emp:
        print("###Employee Found Successfully###")
        print("ID:", emp[0])
        print("Name:", emp[1])
        print("Salary:", emp[2])
        print("Department:", emp[3])
    else:
        print("###ID not found###.")


def empManage():
    print('####Employee Manage####')
    ch=0
    while(ch!='6'):
        print('''Please select option below:
        1.Add employee
        2.Show all employee
        3.Update employee
        4.Delete employee
        5.Search employee
        6.Logout
        ''')
        ch=input("Enter choice:")
        if(ch=='1'):  
            id=int(input('Enter ID:'))
            name=input('Enter Name:')
            sal=int(input('Enter Salary:'))
            dept=input('Enter Deaparment:')
            res=addEmp(id,name,sal,dept)
            print(res)
        elif(ch=='2'):
            showAllEmp()
        elif(ch=='3'):
            print('Warning:ID is not allowed to updated..')
            id=int(input('Enter ID:'))
            res=updEmp(id)
            print(res)
        elif(ch=='4'):
            id=int(input('Enter ID to Deleted:'))
            res=deleteEmp(id)
            print(res)
        elif(ch=='5'):
            id=int(input('Enter Search Id:'))
            searchEmp(id)
        elif(ch=='6'):
            print('Logout')
        else:
            print('Invalid choice...')


def login():
    print('#####Login Page#####')
    uid='admin'
    passw='1234'
    username=input("Enter Username:")
    password=input("Enter Password:")
    if(uid == username and passw ==password):#logical operator (and)for both condition true
        print("Logged in successflly...")
        empManage()#call 
    else:
        print('Invalid credentials...')

def main():    
    ch=0
    while(ch!='2'):#'2'is coverted into string because the user enter string value and we has enter int(input) automated error value the program wiil terimented
        print('####DASHBOARD####')
        print('''Please select option from below:
        1.Login(Admin)
        2.Exit
        ''')
        ch=input('Enter choice:')#compare'2'string
        if(ch=='1'):
            login()#function call
        elif(ch=='2'):
            print('#####Thank you choosing us#####')
        else:
            print('Invalid Choice...')
all_emp_details={}#dictionary empty
main()
# empManage()#for tempery testing

        
        