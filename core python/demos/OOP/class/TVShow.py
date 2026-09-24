class TvShow:
    def __init__(self,name,type,director):
        self.id=id
        self.name=name
        self.type=type
        self.director=director
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def gettype(self):
        return self.type
    def settype(self,newtype):
        self.type=newtype
    def getdirector(self):
        return self.director
    def setdirector(self,newdirector):
        self.director=newdirector
    def display(self):
        print(f"Name{self.name} Type{self.type} director{self.director}")
        
TvShow1=TvShow('MTV Roadies','Reality Show','Sagar More')
print(TvShow1.getdirector())
TvShow1.setdirector('Udit singh')
print(TvShow1.getdirector())
