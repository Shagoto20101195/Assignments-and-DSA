inp = open("input.txt", "r")
output = open("output1.txt", "w")

# Graph Making (Using first input sample method)

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

output.write("{0}\n".format(node))
for i, j in adj_list.items():
    output.write("{0} : {1}\n".format(i, j))

inp.close()
output.close()
