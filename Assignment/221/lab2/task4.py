file1 = open("input4.txt", "r")
file2 = open("output4.txt", "w")

def merge(a, b):
    n1 = len(a)
    n2 = len(b)
    c = [0]*(n1+n2)
    
    left = 0
    right = 0
    ind = 0
    
    while(left < n1 or right < n2):        
        if(left == n1): # If left subarray done taking
            c[ind] = b[right]
            ind += 1
            right += 1
            continue
        
        if(right == n2): # If right subarray done taking
            c[ind] = a[left]
            ind += 1
            left += 1
            continue
        
        if(a[left] <= b[right]):
            c[ind] = a[left]
            ind += 1
            left += 1
        else:
            c[ind] = b[right]
            ind += 1
            right += 1        
    
    return c

def mergesort(arr):
    n = len(arr)
    if(n == 1):
        return arr
    else:
        arr1 = mergesort(arr[0:n//2])
        arr2 = mergesort(arr[n//2:n])
        return merge(arr1, arr2)

# Input processing
n = int(file1.readline())
arr = file1.readline().split(" ")
for i in range(n):
    arr[i] = int(arr[i])
    
# Sorting and output processing
new_arr = mergesort(arr)
for i in range(n):
    file2.write("{0} ".format(new_arr[i]))

file1.close()
file2.close()