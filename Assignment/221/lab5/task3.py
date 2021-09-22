inp = open("task3_input.txt", "r")
output = open("output3.txt", "w")

n = int(inp.readline())
l = inp.readline().replace("\n", "").split(" ")

l.sort()
order = inp.readline().replace("\n", "")

stack = []
seq = ""
jack = 0
jill = 0

for i in order:
    if(i == "J"):
        temp = l.pop(0)
        stack.append(temp)
        jack += int(temp)
        seq += temp
    else:
        temp = stack.pop()
        jill += int(temp)
        seq += temp
        

output.write("{0}\n".format(seq))
output.write("Jack will work for {0} hours\n".format(jack))
output.write("Jill will work for {0} hours\n".format(jill))

inp.close()
output.close()