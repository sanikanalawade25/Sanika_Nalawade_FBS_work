class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def gethr(self):
        return self.hr
    def sethr(self,newhr):
        self.hr=newhr
    def getmin(self):
            return self.min
    def setmin(self,newmin):
        self.min=newmin
    def getsec(self):
        return self.sec
    def setsec(self,newsec):
        self.sec=newsec
    def __add__(self, other):
        totalsec=self.sec+other.sec
        totalmin=self.min+other.min
        totalhr=self.hr+other.hr
        return Time(totalhr,totalmin,totalsec)
    
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
t1=Time(2,45,50)
t2=Time(3,20,30)
print(t1+t2)
        
             
        