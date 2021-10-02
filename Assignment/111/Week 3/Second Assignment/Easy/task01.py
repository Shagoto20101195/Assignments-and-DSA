arr = []
for i in range(0, 10):
    arr.append(int(input("Enter number: ")))
    
arr.reverse()
for i in range(0, 10):
    print(arr[i], end = " ")