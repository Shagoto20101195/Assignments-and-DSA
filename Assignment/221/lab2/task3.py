file1 = open("input3.txt", "r")
file2 = open("output3.txt", "w")

def insertionsort(arr):
    for i in range(n):
        for j in range(i-1, -1, -1):
            if(arr[j][1] < arr[j+1][1]):
                # Swapping roll
                sub = arr[j][0]
                arr[j][0] = arr[j+1][0]
                arr[j+1][0] = sub
                
                # Swapping score
                sub = arr[j][1]
                arr[j][1] = arr[j+1][1]
                arr[j+1][1] = sub
            else:
                break
        

# Input processing
n = int(file1.readline())
roll = file1.readline().split(" ")
res = file1.readline().split(" ")

# [[Roll1, Score1], [Roll2, Score2]....[RollN, ScoreN]]
arr = [[0] * 2 for i in range(n)]

for i in range(n):
    arr[i][0] = int(roll[i])
    arr[i][1] = int(res[i])
    
# Sorting and output processing
insertionsort(arr)
for i in range(n):
    file2.write("{0} ".format(arr[i][0]))

    
file1.close()
file2.close()