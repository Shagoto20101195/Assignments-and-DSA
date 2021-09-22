inp = open("input.txt", "r")
output = open("output3.txt", "w")

def dfs(node, end):
    visited[node] = 1
    output.write("{0} ".format(node))
    
    for i in adj_list[node]:
        if(visited[i] == 0):
            dfs(i, end)
        if(visited[end] == 1): # If destination reached
            return
  
# Graph Making
node = int(inp.readline())
edges = int(inp.readline())

adj_list = {}

for i in range(1, node+1):
    adj_list[i] = []

for i in range(edges):
    temp = inp.readline().split(" ")
    u = int(temp[0])
    v = int(temp[1])
    adj_list[u].append(v)

visited = [0]*(node+1) # 1-index based
output.write("Places: ")

# DFS for all nodes
for i in range(1, node+1):
    if(visited[i] == 0):
        dfs(i, 12)
    if(visited[12] == 1): # If destination reached
        break

inp.close()
output.close()