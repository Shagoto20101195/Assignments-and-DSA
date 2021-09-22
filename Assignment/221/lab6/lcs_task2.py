inp = open("input2.txt", "r")
output = open("output2.txt", "w")

x = inp.readline()
y = inp.readline()
z = inp.readline()

x_len = len(x)
y_len = len(y)
z_len = len(z)

cost = [[[None]*(z_len+1) for i in range(y_len+1)] for j in range(x_len+1)]
direction = [[[None]*(z_len+1) for i in range(y_len+1)] for j in range(x_len+1)]


for i in range(x_len+1):
    for j in range(y_len+1):
        for k in range(z_len+1):
            
            if(i == 0 or j == 0 or k == 0):
                cost[i][j][k] = 0
                direction[i][j][k] = None
            
            else:
                
                if(x[i-1] == y[j-1] and x[i-1] == z[k-1]):
                    cost[i][j][k] = cost[i-1][j-1][k-1] + 1
                    direction[i][j][k] = "diagonal"
                
                else:
                    if(cost[i-1][j][k] >= cost[i][j-1][k]):
                        _max = cost[i-1][j][k]
                        
                        if(_max >= cost[i][j][k-1]):
                            cost[i][j][k] = _max
                            direction[i][j][k] = "up-up-left"
                        else:
                            _max = cost[i][j][k-1]
                            cost[i][j][k] = _max
                            direction[i][j][k] = "left-up-up"
                    
                    else:
                        _max = cost[i][j-1][k]
                        if(_max >= cost[i][j][k-1]):
                            cost[i][j][k] = _max
                            direction[i][j][k] = "up-left-up"
                        else:
                            _max = cost[i][j][k-1]
                            cost[i][j][k] = _max
                            direction[i][j][k] = "left-up-up"

output.write("{0}".format(cost[x_len][y_len][z_len]))

inp.close()
output.close()
