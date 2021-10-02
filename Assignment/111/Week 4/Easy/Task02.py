s = input().split(", ")
my_dict = {}
for x in s:
    temp = x.split(":")
    my_dict[temp[0]] = int(temp[1])

print("Minimum:", min(my_dict, key = my_dict.get))
print("Maximum:", max(my_dict, key = my_dict.get))