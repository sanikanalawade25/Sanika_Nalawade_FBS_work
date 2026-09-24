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
p1=CricketPlayer(101,'Virat',34)
print(p1)



        