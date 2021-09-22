file1 = open("input1.txt", "r")
file2 = open("output1.txt", "w")

def bubbleSort(arr):
    for i in range(len(arr)-1):
        count = 0
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                count += 1
        
        if(count == len(arr) - i - 1):
            break

"""
The swapping in Bubble Sort takes place if a larger number
can be swapped to right (higher index).

For best case, that is if the array is initially sorted, no swap will
take place. A count is taken if no swap takes place.

Therefore, if the number of checkings matches with the count, it means
the array is sorted and we can break out of outer loop.

For only one iteration upto almost n, we can say:

Time complexity for best case: O(n)
"""


# Input processing
n = int(file1.readline())
arr = file1.readline().split(" ")
for i in range(n):
    arr[i] = int(arr[i])

# Sorting and output processing
bubbleSort(arr)
for i in range(n):
    file2.write("{0} ".format(arr[i]))
    
file1.close()
file2.close()
