inp = open("task2_input.txt", "r")
output = open("output2.txt", "w")

# l = list of tasks
# l[i][1] = i-th task's start time
# l[i][0] = i-th task's finish time
l = []

temp = inp.readline().split(" ")
n = int(temp[0])
m = int(temp[1])

for i in range(n):
    temp = inp.readline().split(" ")
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    l.append([])
    l[i].append(temp[1])
    l[i].append(temp[0])

l.sort()
# d = {i: [[task1f, task1s], [task2f, task2s], ...], i+1: [...], ...}
# d[i] = i-th person's list of tasks
# d[i][j][1] = i-th person's j-th task's start time
# d[i][j][0] = i-th person's j-th task's finish time
d = {}

for i in range(1, m+1):
    d[i] = []
    
# First task to first person
d[1].append(l[0])
count = 1

for i in range(1, n):
    for person in range(1, m+1):
        
        # If the person has previously completed any task
        if(len(d[person]) >= 1 and l[i][1] >= d[person][len(d[person])-1][0]):
            d[person].append(l[i])
            count += 1
            break
        
        # If the person didn't do any task
        elif(len(d[person]) == 0):
            d[person].append(l[i])
            count += 1
            break

output.write("{0}\n".format(count))

inp.close()
output.close()