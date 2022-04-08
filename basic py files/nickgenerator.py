kelimeler = []
for i in range (15):
    kelime = str(input("kelime giriniz :"))
    if (kelime == ""):
        break
    kelimeler.append(kelime)
def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst]  
    l = [] 
    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l
data = permutation(kelimeler)
def nickgenerator():
    nicks = []
    nick = ""
    for i in range(len(data)):
        for j in range(len(kelimeler)):
                nick = nick + data[i][j][j]
        nicks.append(nick)
        nick=""
    return nicks
print (nickgenerator())