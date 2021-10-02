from datetime import date

today = date.today()
today = today.strftime("%Y - %m - %d")
today = int(today[0: 4: 1])

def profit(*s):
    profit = None
    year = today - int(s[2][0: 4: 1])
    if(year < 5):
        profit = s[1] * 10 // 100
    elif(year >= 5 and year <= 10):
        profit = s[1] * 10 // 100
        profit += 5000
    else:
        profit = s[1] * 15 // 100
        profit += 15000
    
    print(s[0]+":",profit)
    
profit("Alice", 20000, "2017-03-21")