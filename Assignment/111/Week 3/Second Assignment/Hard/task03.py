n = int(input("Enter number of students: "))
k = int(input("Enter limit: "))

arr = []
for i in range(0, n):
    arr.append(int(input("Enter number of participation: ")))

arr.sort()
count = 0
for i in range(0, n):
    if(arr[i] + k <= 5):
        count += 1

print(count // 3)