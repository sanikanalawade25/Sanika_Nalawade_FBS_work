class StudentFBS:
    stCount=0
    def __init__(self,FRN,Name,Batch):
        self.FRN=FRN
        self.Name=Name
        self.Batch=Batch
        StudentFBS.stCount+=1
    
    def getFRN(self):
        return self.FRN
    def setFRN(self,newFRN):
        self.FRN=newFRN
    def getName(self):
        return self.Name
    def setName(self,newName):
        self.Name=newName
    def getBatch(self):
        return self.Batch
    def setBatch(self,newBatch):
        self.Batch=newBatch
    def display(self):
        print(f"FRN={self.FRN} Name={self.Name} Batch={self.Batch}")
#StusentFBS End
class PlStudent(StudentFBS):
    def __init__(self, FRN, Name, Batch,CName):
        super().__init__(FRN, Name, Batch)  #Inheritance
        self.CName=CName
    def getCName(self):
        return self.CName
    def setCName(self,newCname):
        self.CName=newCname
    
    def display(self):
        super().display()
        print(f"CName={self.CName}")
    

StudentFBS1=StudentFBS(16,'Sanika','June26')
StudentFBS2=StudentFBS(13,'Sai','June25')
StudentFBS3=PlStudent(12,'Sahil','June21','Google')
print(StudentFBS.stCount)

# print(StudentFBS1.getFRN())
# StudentFBS1.setFRN('15')
# print(StudentFBS1.getFRN())



        