Fibo = [1, 2]
sum = 2
while Fibo[-1] < 4000000:
    Fibo.append(Fibo[-1]+Fibo[-2])
    if (Fibo[-1]%2==0):
        sum = sum + Fibo[-1]
print(sum)
