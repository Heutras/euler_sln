sum = pow((100*101/2),2)
sumsqr = 0
for i in range(1,101):
    sumsqr = sumsqr + i**2
fnl = sum - sumsqr
print(fnl)