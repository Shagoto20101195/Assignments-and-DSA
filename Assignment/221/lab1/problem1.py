file = open("input.txt", "r")
file2 = open("output.txt", "w")
file3 = open("record.txt", "w")

def isPalin(word):
    if(word == None):
        return False
    
    n = len(word)
    
    for i in range(0, n // 2):
        if(word[i] != word[n - i - 1]):
            return False
    return True

size = 0
odd = 0
even = 0
nor = 0
palin = 0
npalin = 0

for line in file:
    size += 1
    inp = line.split(" ")
    inp[1] = inp[1].replace("\n", "")
    
    if("." in inp[0]):
        nor += 1
        file2.write("{0} cannot have parity and ".format(inp[0]))
        
    else:
        temp = int(inp[0])
        
        if(temp % 2 == 0):
            even += 1
            file2.write("{0} has even parity and ".format(inp[0]))
        else:
            odd += 1
            file2.write("{0} has odd parity and ".format(inp[0]))
    
    if(isPalin(inp[1])):
        palin += 1
        file2.write("{0} is a palindrome\n".format(inp[1]))
    else:
        npalin += 1
        file2.write("{0} is not a palindrome\n".format(inp[1]))

file3.write("Percentage of odd parity: {0}%\n".format(odd * 100 // size))
file3.write("Percentage of even parity: {0}%\n".format(even * 100 // size))
file3.write("Percentage of no parity: {0}%\n".format(nor * 100 // size))
file3.write("Percentage of palindrome: {0}%\n".format(palin * 100 // size))
file3.write("Percentage of non-palindrome: {0}%".format(npalin * 100 // size))
    
file.close()
file2.close()
file3.close()
