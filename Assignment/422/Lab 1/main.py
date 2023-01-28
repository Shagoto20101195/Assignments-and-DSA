import heapq
inp = open("Input file.txt", "r")

heuristic_values = {}
pq = []
heapq.heapify(pq)

for i in range(20):
    temp = inp.readline().replace("\n", "").split(" ")
    
    heuristic_values[temp[0][0]] = int(temp[1])

print(heuristic_values)
print(pq)
