# Task 03

class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def sleep(self, hour = None):
        if(hour == None):
            return "{:}'s duration is unknown thus should have only bamboo leaves".format(self.name)
        elif(hour >= 3 and hour <= 5):
            return "{:} sleeps {:} hours daily and should have Mixed Veggies".format(self.name, hour)
        elif(hour >= 6 and hour <= 8):
            return "{:} sleeps {:} hours daily and should have Eggplant & Tofu".format(self.name, hour)
        elif(hour >= 9 and hour <= 11):
            return "{:} sleeps {:} hours daily and should have Broccoli Chicken".format(self.name, hour)

panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))

print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())