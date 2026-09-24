class Place:
    def __init__(self,name,location,climate):
        self.name=name
        self.location=location
        self.climate=climate
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def getlocation(self):
        return self.location
    def setlocation(self,newlocation):
        self.location=newlocation
    def getclimate(self):
        return self.climate
    def setclimate(self,newclimate):
        self.climate=newclimate
    
    def display(self):
        print(f"Name{self.name} Location{self.location} Climate{self.climate}")

place=Place('Satara','Satara Maharashtra','Cool')
print(place.getname())
place.setname('Pune')
print(place.getname())
