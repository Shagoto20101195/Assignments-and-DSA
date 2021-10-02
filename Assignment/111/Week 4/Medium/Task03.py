s = input().split(", ")
my_dict = {}
for x in s:
    temp = x.split(" : ")
    
    if(temp[1] in my_dict):
        t = my_dict.get(temp[1])
        t.append(temp[0])
        my_dict[temp[1]] = t
    else:
        my_dict[temp[1]] = [temp[0]]

print(my_dict)