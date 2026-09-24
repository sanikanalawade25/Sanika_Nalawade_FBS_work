class Player:
    def __init__(self,jrno,name):
        self.jrno=jrno
        self.name=name
    def getjrno(self):
        return self.jrno
    def setjrno(self,newjrno):
        self.jrno=newjrno
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def __str__(self):
        return f"jrno={self.jrno}\t Name={self.name}"
class CricketPlayer(Player):
    def __init__(self, jrno, name,runs):
        super().__init__(jrno, name)
        self.runs=runs
    def getruns(self):
        return self.runs
    def setruns(self,newruns):
        self.runs=newruns
    def __str__(self):
        return super().__str__()+f"\truns={self.runs}"

class RunjPlayer(CricketPlayer):  #multilevel
    
    def __init__(self, jrno, name, runs,zone):
        super().__init__(jrno, name, runs)
        self.zone=zone
    def getzone(self):
        return self.zone
    def setzone(self,newzone):
        self.zone=newzone
    def __str__(self):
        return super().__str__()
p1=CricketPlayer(101,'Virat',34)
rp=RunjPlayer(10,'ABC',14,'XYZ')
# print(p1)
print(rp)



        
