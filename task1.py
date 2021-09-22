inp = open("input1.txt", "r")
output = open("output1.txt", "w")

dic = {
       "Y" : "Yasnaya",
       "P" : "Pochinki",
       "S" : "School",
       "R" : "Rozhok",
       "F" : "Farm",
       "M" : "Mylta",
       "H" : "Shelter",
       "I" : "Prison"
       }
  

n = int(inp.readline())
x = inp.readline()
y = inp.readline()

x_len = len(x)
y_len = len(y)

cost = [[None]*(y_len+1) for i in range(x_len+1)]
direction = [[None]*(y_len+1) for i in range(x_len+1)]

for i in range(x_len+1):
    cost[i][0] = 0
    direction[i][0] = None

for i in range(y_len+1):
    cost[0][i] = 0
    direction[0][i] = None

for i in range(1, x_len+1):
    for j in range(1, y_len+1):
        if(x[i-1] == y[j-1]):
            cost[i][j] = cost[i-1][j-1] + 1
            direction[i][j] = "diagonal"
        
        elif(cost[i-1][j] >= cost[i][j-1]):
            cost[i][j] = cost[i-1][j]
            direction[i][j] = "up"
            
        else:
            cost[i][j] = cost[i][j-1]
            direction[i][j] = "left"

ans = ""
i = x_len
j = y_len
while(i > 0 and j > 0):
    if(direction[i][j] == "diagonal"):
        ans = x[i-1] + ans
        i -= 1
        j -= 1
    elif(direction[i][j] == "up"):
        i -= 1
    else:
        j -= 1

for i in ans:
    output.write("{0} ".format(dic[i]))

output.write("\nCorrectness of prediction: {0}%".format(len(ans) * 100 // n))

inp.close()
output.close()