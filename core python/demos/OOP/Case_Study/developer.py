from Emp import Emp

class Developer(Emp):
    def __init__(self, id, name, sal, Bonous):
        super().__init__(id, name, sal)
        self.Bonous = Bonous

    def getBonous(self):
        return self.Bonous

    def setBonous(self, newBonous):
        self.Bonous = newBonous

    def calSal(self):                  # Polymorphism
        return self.Bonous + self.sal

    def display(self):
        print(self)
        print(f"Bonous = {self.Bonous}")
        print(f"Total Salary = {self.calSal()}")