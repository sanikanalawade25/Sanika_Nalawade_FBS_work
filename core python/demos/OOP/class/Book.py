class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def gettitle(self):
        return self.title
    def settitle(self,newtitle):
        self.title=newtitle
    def getauthor(self):
        return self.author
    def setauthor(self,newauthor):
        self.author=newauthor
    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice
    

    def display(self):
        print(f"Title{self.title} Author{self.author} Price{self.price}")

book1=Book('Wings of Fire','A.P.J Abdul Kalam',250)
book2=Book('Shyamchi Aai','Sane Guruji',300)

print(book1.getprice())
book1.setprice('300')
print(book1.getprice())



