class MyExeceptionUser(Exception):
    def __init__(self,*args):
        print("I am from my exception")
    def __str__(self):
        return "My excepetion object"
        