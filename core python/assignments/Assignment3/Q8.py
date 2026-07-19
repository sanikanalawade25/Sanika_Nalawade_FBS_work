# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random
user_id=input("Enter User_id:")
password=input("Enter Password :")
if(user_id=="Sanika" and password=="123"):
    captcha=random.randint(1000,9999)
    print(captcha)
    chooser_captcha=int(input("Enter the captcha:"))
    if(chooser_captcha==captcha):
        print("User Login Succefully")
    else:
        print("Invalid captcha")
else:
    print("User_id and password Invalid")