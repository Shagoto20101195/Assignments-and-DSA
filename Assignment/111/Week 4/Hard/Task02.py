def get_key(char):
    for key,val in d.items():
        if(val.count(char) > 0):
            return str(key)+" "+str(val.index(char) + 1)
        
d = {0:[" "], 1:[".",",","?","!",":"], 2:["A","B","C"], 3:["D","E","F"], 4:["G","H","I"], 5:["J","K","L"], 6:["M","N","O"], 7:["P","Q","R","S"], 8:["T","U","V"], 9:["W","X","Y","Z"]}
s = input()
s = s.upper()
for x in s:
    result = get_key(x).split(" ")
    print(result[0] * int(result[1]), end = "")