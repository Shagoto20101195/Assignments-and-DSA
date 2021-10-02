#task 02

n = int(input("Number of lists: "))

max_sum = 0
ans = []
for i in range(0, n):
    l = input().split(" ")
    temp = 0
    for j in l:
        temp += int(j)
    
    if(temp > max_sum):
        max_sum = temp
        ans = l
    

print(max_sum)
print(ans)