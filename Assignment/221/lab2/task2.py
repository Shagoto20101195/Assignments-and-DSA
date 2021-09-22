file1 = open("input2.txt", "r")
file2 = open("output2.txt", "w")

def selectionsort(arr, m):
    for i in range(m):
        ind = i
        elem = arr[i]
        for j in range(i+1, n):
            if(arr[j] < elem):
                ind = j
                elem = arr[j]
        temp = arr[i]
        arr[i] = arr[ind]
        arr[ind] = temp

# Input processing
inp1 = file1.readline().split(" ")
n = int(inp1[0])
m = int(inp1[1])

inp2 = file1.readline().split(" ")
for i in range(n):
    inp2[i] = int(inp2[i])
       
# Sorting and output processing
selectionsort(inp2, m)
for i in range(m):
    file2.write("{0} ".format(inp2[i]))

file1.close()
file2.close()