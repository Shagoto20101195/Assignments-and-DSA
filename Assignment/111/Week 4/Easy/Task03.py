index = 1
my_dict = {}
while(index <= 10):
    n = int(input("Enter number: "))
    
    if(n in my_dict):
        print("Number already taken. Enter different number.")
        continue
    else:
        my_dict[n] = 1
    index += 1