arr = []
while(True):
    n = input()
    
    if(n == "STOP"):
        break
    else:
        n = int(n)
        arr.append(n)
        
check = []
for i in range(0, len(arr)):
    if(check.count(arr[i]) > 0):
        continue
    else:
        print(arr[i], "-", arr.count(arr[i]), "times")
        check.append(arr[i])