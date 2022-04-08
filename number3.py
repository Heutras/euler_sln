num = 600851475143
div = []
i = 2
while(i<num) or (num!=1):
    if(num%i==0):
        div.append(i)
        num = num / i
    else:
        i = i + 1
div_sorted = sorted(div)
print(div_sorted[-1])