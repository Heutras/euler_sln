all_num = []
def checkAmicable(n) :
    i = 1
    j = 1
    temp_sum = 0
    temp_sum1 = 0
    while i <= n :
        if (n % i==0 and n != i) :
            temp_sum += i
        i = i + 1
    while j <= temp_sum:
        if (temp_sum % j == 0 and temp_sum != j):
            temp_sum1 += j
        j += 1
    if (n != temp_sum and n==temp_sum1):
        all_num.append(n)
        all_num.append(temp_sum)
for i in range(10000,0,-1):
    checkAmicable(i)
print(all_num)
all_sum = sum(all_num)
print("We are diving the sum of this array to 2, because there is 2 instances for each number")
all_sum = sum(all_num) / 2
print("result =",all_sum)