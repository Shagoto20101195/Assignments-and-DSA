m = int(input("Enter marks: "))

if(m >= 90):
    print("A")
elif(m >= 85 and m <= 89):
    print("A-")
elif(m >= 80 and m <= 84):
    print("B+")
elif(m >= 75 and m <= 79):
    print("B")
elif(m >= 70 and m <= 74):
    print("B-")
elif(m >= 65 and m <= 69):
    print("C+")
elif(m >= 60 and m <= 64):
    print("C")
elif(m >= 57 and m <= 59):
    print("C-")
elif(m >= 55 and m <= 56):
    print("D+")
elif(m >= 52 and m <= 54):
    print("D")
elif(m >= 50 and m <= 51):
    print("D-")
else:
    print("F")