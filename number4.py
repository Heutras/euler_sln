max = 0
for i in range(100,999):
    for j in range(100,999):
        multi = i * j
        if (str(multi)[0]==str(multi)[-1]) and (str(multi)[1]==str(multi)[-2]) and (str(multi)[2]==str(multi)[-3]):
            if (multi>max):
                max = multi
print(max)