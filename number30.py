def superfive(num):
    temp = str(num)
    sum = 0
    for i in temp:
        sum += int(i)**5
    if (num == sum):
        return True
    else:
        return False
b = []
for i in range(1000000,10,-1):
    temp = superfive(i)
    if(temp == True):
        b.append(i)
sum_all = 0
for x in b:
    sum_all += x
print("result =",sum_all)