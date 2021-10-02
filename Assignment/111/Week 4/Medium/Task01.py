d1 = {}
n1 = input().split(", ")
for x in n1:
    temp = x.split(": ")
    d1[temp[0]] = int(temp[1])

d2 = {}
n2 = input().split(", ")
for x in n2:
    temp = x.split(": ")
    d2[temp[0]] = int(temp[1])
    
l = []
d3 = {}

for x in d1:
    if(x in d2):
        temp = d1.get(x) + d2.get(x)
        d3[x] = temp
        if(l.count(d3[x]) == 0):
            l.append(d3[x])
    else:
        d3[x] = d1.get(x)
        if(l.count(d3[x]) == 0):
            l.append(d3[x])

for x in d2:
    if(x not in d3):
        d3[x] = d2.get(x)
        if(l.count(d3[x]) == 0):
            l.append(d3[x])

l.sort()
print(d3)
print("Values:", tuple(l))