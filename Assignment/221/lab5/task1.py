inp = open("task1_input.txt", "r")
output = open("output1.txt", "w")

# l = list of tasks
# l[i][1] = i-th task's start time
# l[i][0] = i-th task's finish time
l = []

n = int(inp.readline())
for i in range(n):
    temp = inp.readline().split(" ")
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    l.append([])
    l[i].append(temp[1])
    l[i].append(temp[0])

l.sort()
ans = []
ans.append(l[0])
finish = l[0][0]

for i in range(1, n):
    if(l[i][1] >= finish):
        finish = l[i][0]
        ans.append(l[i])

output.write("{0}\n".format(len(ans)))
for i in ans:
    output.write("{0} {1}\n".format(i[1], i[0]))

inp.close()
output.close()
