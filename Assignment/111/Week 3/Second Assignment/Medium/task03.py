#task 03

l1 = input().split(" ")
l2 = input().split(" ")

ans = []
for i in l1:
    for j in l2:
        ans.append(int(i) * int(j))
        
print(ans)