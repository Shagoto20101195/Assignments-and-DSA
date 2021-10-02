# task 03

class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True
        
wadiya = Wadiya()
temp1 = wadiya.name
print("Part 1:")
print("Name of President:", wadiya.name)
print("Designation:", wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)

print("Part 2:")
wadiya.name = "Donald Trump"
wadiya.designation = "President"
wadiya.num_of_wife = 1
wadiya.dictator = False
temp2 = wadiya.name
print("Name of President:", wadiya.name)
print("Designation:", wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)

if(temp1 != temp2):
    print("Previous information lost")
else:
    print("No, changing had no effect on previous value")