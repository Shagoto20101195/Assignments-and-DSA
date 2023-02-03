import heapq
inp = open("Input file.txt", "r")

heuristic_values = {}
location = {}
connections = {}
ans = []
path_ans = {}
pq = []
heapq.heapify(pq)

while True:
    try:
        temp = inp.readline().replace("\n", "").split(" ")
        
        location[temp[0][0]] = temp[0]
        heuristic_values[temp[0][0]] = int(temp[1])
        connections[temp[0][0]] = {}
        #print(temp)
        for i in range(2, len(temp), 2):
            connections[temp[0][0]][temp[i][0]] = int(temp[i+1])
    except:
        break

print(connections)

start = input("Start node: ")
end = input("End node: ")


if(len(ans) == 0):
    print("NO PATH FOUND")
else:
    dist = min(ans)
    route = path_ans[dist]
    print("Path:", end = " ")
    for i in route:
        print(location[i], end = " ")
        
        if(i != end[0]):
            print("->", end = " ")
    print()
    print(f"Total distance: {dist} km")