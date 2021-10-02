# task 04

class Joker:
    def __init__(self, name, typ, psy):
        self.name = name
        self.power = typ
        self.is_he_psycho = psy
        

j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')
    
print("The object j1 and j2 have different address.")
print("j2.name was assigned with 'Heath Ledger'. So the instance variables are same.")