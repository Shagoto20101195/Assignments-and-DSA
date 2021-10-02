while(True):
    n = input()
    
    if(n == "STOP"):
        break
    else:
        n = int(n)
        arr = []
        dif = []
        
        for i in range(0, n):
            arr.append(int(input()))
            
            if(i > 0):
                dif.append(abs(arr[i] - arr[i - 1]))
        
        dif.sort()
        check = True
        for i in range(0, len(dif)):
            if(i+1 != dif[i]):
                check = False
                break
        
        if(check):
            print("UB Jumper")
        else:
            print("Not UB Jumper")