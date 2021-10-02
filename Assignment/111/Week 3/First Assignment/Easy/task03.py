s = input("Enter word: ")

if(len(s) < 4):
    print(s)
elif(s.endswith("ful")):
    print(s+"ly")
else:
    print(s+"ful")