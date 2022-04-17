def checkAbundant(n) :
    i = 1
    temp = []
    while i <= n :
        if (n % i==0 and n != i) :
            temp.append(i)
        i = i + 1
    if (sum(temp) > n):
        return True
    else:
        return False

start = 500
all_num = []
def SumOfAbundants(n,k) :
    if checkAbundant(n) and checkAbundant(k) is True:
        return False
    else:
        return True

result = 0
for i in range(24,28124):
    for j in range (12,i):
        temp = i -j
        if SumOfAbundants(j,temp) is False:
            #result += i
            break
            #print("kontrol edilen", i, "toplamı için ilk seçilen",j,"ikinci seçilen",temp,"sonuç",SumOfAbundants(j,temp),checkAbundant(j),checkAbundant(temp))
        else:
            #print("cevap bu:",i)
            if i not in all_num:
                all_num.append(i)
#print(all_num)
for i in (0,25):
    if i not in all_num:
        all_num.append(i)
print(sum(all_num))