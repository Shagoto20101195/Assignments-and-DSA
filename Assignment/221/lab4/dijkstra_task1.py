inp = open("input1.txt", "r")
output = open("output1.txt", "w")

import heapq

def dijkstra(graph, source):
    dist = [0] * len(graph)
    prev = [0] * len(graph)
    visited = [0] * len(graph)
    pq = []
    heapq.heapify(pq)
    
    for i in range(1, len(graph)):
        if(i != source):
            dist[i] = 10000000000000
            prev[i] = 0
        
    heapq.heappush(pq, (0, source))
    while(len(pq) > 0):
        d, u = heapq.heappop(pq)
        
        if(visited[u] == 1):
            continue
        visited[u] = 1
        
        for i in graph[u]:
            if(d + i[1] < dist[i[0]]):
                dist[i[0]] = d + i[1]
                prev[i[0]] = u
                heapq.heappush(pq, (dist[i[0]], i[0]))
    
    
    return dist[len(graph)-1]


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
        
        adj_list[u].append([v, w])
    
    ans = dijkstra(adj_list, 1)
    output.write("{0}\n".format(ans))
    

inp.close()
output.close()
