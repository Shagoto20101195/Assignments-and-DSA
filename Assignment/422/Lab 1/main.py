import heapq
inp = open("Input file.txt", "r")

visited_nodes = {} # Not to traverse visited node again (True means visited)
heuristic_values = {}
location = {} # e.g. {'A' : 'Arad'}
connections = {} # e.g. {'A': {'Z': 75, 'T': 118, 'S': 140}}
ans = 1000000 # Taking to be infinite
path_ans = ""
pq = [] # Priority Queue
heapq.heapify(pq)

while True:
    try:
        temp = inp.readline().replace("\n", "").split(" ")
        
        location[temp[0][0]] = temp[0]
        visited_nodes[temp[0][0]] = False
        heuristic_values[temp[0][0]] = int(temp[1])
        connections[temp[0][0]] = {}
        
        for i in range(2, len(temp), 2):
            connections[temp[0][0]][temp[i][0]] = int(temp[i+1])
            visited_nodes[temp[i][0]] = False
    except:
        break

start = input("Start node: ")
end = input("End node: ")

for i in connections[start[0]]:
    cost = connections[start[0]][i] + heuristic_values[i]
    path = start[0] + i
    heapq.heappush(pq, (cost, path))

visited_nodes[start[0]] = True
while(len(pq) > 0):
    cost, path = heapq.heappop(pq)
    
    if(visited_nodes[path[len(path)-1]]): # To avoid infinite loop
        continue

    visited_nodes[path[len(path)-1]] = True
    for i in connections[path[len(path)-1]]:
        new_path = path + i
        new_cost = cost - heuristic_values[path[len(path)-1]] + heuristic_values[i] + connections[path[len(path)-1]][i]
        heapq.heappush(pq, (new_cost, new_path))
        
        if(new_path[len(new_path)-1] == end[0] and new_cost < ans):
            ans = new_cost
            path_ans = new_path

if(path_ans == ""):
    print("NO PATH FOUND")
else:
    print("Path:", end = " ")
    for i in path_ans:
        print(location[i], end = " ")
        
        if(i != end[0]):
            print("->", end = " ")
    print()
    print(f"Total distance: {ans} km")