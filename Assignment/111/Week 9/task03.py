# Task 03

class Dates:
    def __init__(self, date):
        self.date = date
    def getDate(self):
        return self.date
    def __eq__(self, other):
        if(self.date == other.date):
            return True
        else:
            return False
    @classmethod
    def toDashDate(cls, date):
        return cls(date.replace("/", "-"))

date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2= Dates.toDashDate(dateFromDB)
if(date1.getDate() == date2.getDate()):
    print("Equal")
else:
    print("Unequal")

print()
print("The returned value of two instance variables are same after operator overloading")