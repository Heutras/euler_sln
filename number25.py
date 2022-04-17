oldval = 1
newval = 1
tempval = 0
n = 2
while (len(str(newval)) < 1000):
    tempval = newval
    newval = tempval + oldval
    oldval = tempval
    n += 1
print("result iteration: ",n,"result number: ",newval)