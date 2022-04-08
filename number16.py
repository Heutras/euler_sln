number = 2**1000
str_num = str(number)
sum = 0
for i in range(len(str_num)):
    sum = sum + int(str_num[i])
print("sonuc =", sum)