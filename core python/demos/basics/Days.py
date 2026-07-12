Days=int(input("Enter Days:"))
Years=Days//365
Days=Days%365
Weeks=Days//7
Days=Days%7
print(f'Years={Years} Weeks={Weeks} and Days={Days}.')