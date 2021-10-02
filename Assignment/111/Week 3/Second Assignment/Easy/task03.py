arr = []
arr.append(int(input("Enter number: ")))

index = 1
while(index <= 9):
    n = int(input("Enter number: "))
    
    if(arr.count(n) > 0):
        print("Number already taken. Enter different number: ")
        continue
    else:
        arr.append(n)
    index += 1