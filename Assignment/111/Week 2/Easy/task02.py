def BMI(x, y):
    x = x**2 / 10000
    x = y / x
    x = "{0:5.1f}".format(x)
    return x
        
a = int(input("Enter height: "))
b = int(input("Enter weight: "))
ans = float(BMI(a, b))

if(ans < 18.5):
    print("Score is ",ans,". You are Underweight", sep = "")
elif(ans >= 18.5 and ans <= 24.9):
    print("Score is ",ans,". You are Normal", sep = "")
elif(ans >= 25 and ans <= 30):
    print("Score is ",ans,". You are Overweight", sep = "")
else:
    print("Score is ",ans,". You are Obese", sep = "")