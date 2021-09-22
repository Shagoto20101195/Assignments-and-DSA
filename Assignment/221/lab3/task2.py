inp = open("input.txt", "r")
output = open("output2.txt", "w")

def bfs(start, end):
    visited = [0]*(node+1) # 1-index based
    queue = []
    queue.append(start)
    visited[start] = 1
    
    while(len(queue) > 0):
        m = queue.pop(0)
        output.write("{0} ".format(m))
        
        if(m == end):
            break
        for i in adj_list[m]:
            if(visited[i] == 0):
                queue.append(i)
                visited[i] = 1
    
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

output.write("Places: ")
bfs(1, 12)

inp.close()
output.close()