def find_vowel(s):
    count = 0
    vowels = ""
    for i in s:
        if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            vowels += i
            count += 1
        elif(i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            vowels += i
            count += 1
            
    if(count == 0):
        print("No vowels in the name")
    else:
        print("Vowels: ", end = "")
        
        index = 0
        while(index < len(vowels)):
            if(index == len(vowels) - 1):
                print(vowels[index], end = ".")
            else:
                print(vowels[index], end = ", ")
            index += 1
        
        print(" Total number of vowels:", count)
                

s = input("Enter name: ")
find_vowel(s)