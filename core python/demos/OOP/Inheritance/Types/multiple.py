class Mechinical:
    def __init__(self):
        print("I am from mec")
    def __str__(self):
        return"Mec ka object"
    def getBaranch(self):
        print("Mechinical Branch")
class Electronic:
    def __init__(self):
        print("I sm from Electronic")
    def __str(self):
        return"object of electronic"
    def getBaranch(self):
        print(" I am from Electronic Branch")
class Mecalnicax(Mechinical,Electronic):
    def __init__(self):
        super().__init__()
        print("construct of Mectronix get called")
    def __str__(self):
        return super().__str__()+"\n onject of mectronix"
    def getBaranch(self):
        print("I am from Mecalniax")
        return super().getBaranch()
    
m=Mecalnicax()
# print(m)
m.getBaranch()