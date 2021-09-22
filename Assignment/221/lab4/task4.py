inp = open("input4.txt", "r")
output = open("output4.txt", "w")

import heapq

def dijkstra(graph, source):
    dist = [0] * len(graph)
    prev = [0] * len(graph)
    visited = [0] * len(graph)
    pq = []
    heapq.heapify(pq)
    
    for i in range(1, len(graph)):
        if(i != source):
            dist[i] = -10000000000000
            prev[i] = 0
        
    heapq.heappush(pq, (-10000000000000, source))
    while(len(pq) > 0):
        d, u = heapq.heappop(pq)
        
        if(visited[u] == 1):
            continue
        visited[u] = 1
        
        for i in graph[u]:
            if(min(-d, -i[1]) > dist[i[0]]):
                dist[i[0]] = min(-d, -i[1])
                prev[i[0]] = u
                heapq.heappush(pq, (-dist[i[0]], i[0]))
    
    return dist


t = int(inp.readline())
for case in range(t):
    adj_list = {}
    line = inp.readline().split(" ")
    n = int(line[0])
    m = int(line[1])
    
    for i in range(n+1):
        adj_list[i] = []
    
    for i in range(m):
        temp = inp.readline().split(" ")
        u = int(temp[0])
        v = int(temp[1])
        w = int(temp[2])
        
        adj_list[u].append([v, -w])
    
    s = int(inp.readline())
    
    temp = dijkstra(adj_list, s)        
    for i in range(1, n+1):
        if(temp[i] == -10000000000000):
            temp[i] = -1
        output.write("{0} ".format(temp[i]))
    
    output.write("\n")

inp.close()
output.close()