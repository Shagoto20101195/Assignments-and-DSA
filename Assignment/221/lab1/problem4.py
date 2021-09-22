file = open("input4.txt", "r")
file2 = open("output4.txt", "w")

n = int(file.readline())
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(n)]
c = [[0] * n for i in range(n)]

"""
2
5 8
3 8
3 8
8 9

Output
79 112
73 96
"""

"""
3
10 20 10
4 5 6
2 3 5
3 2 4
3 3 9
4 4 2

Output
130 120 240
51 47 73
35 33 45
"""

for i in range(2*n):
    inp = file.readline().split(" ")
    
    if(i < n):
        for j in range(n):
            a[i][j] = int(inp[j])
 
    else:
        for j in range(n):
            b[i - n][j] = int(inp[j])
            
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]


for i in range(n):
    ans = ""
    for j in range(n):
        ans += "{0} ".format(c[i][j])
    file2.write(ans+"\n")

file.close()
file2.close()