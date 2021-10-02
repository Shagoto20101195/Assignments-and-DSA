def calc(t, location = "mohakhali"):
    tax = t * 8 / 100
    if(location == "mohakhali"):
        return t+tax+40
    else:
        return t+tax+60

a = input("Enter burger type: ")
b = input("Enter location: ")

price = None
if(a == "BBQ Chicken Cheese Burger"):
    price = 250
elif(a == "Beef Burger"):
    price = 170
elif(a == "Naga Drums"):
    price = 200
print(calc(price, b))