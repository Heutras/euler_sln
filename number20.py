# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
x = 1
sum = 0
for i in range(2,101):
    x = x * i
y = str(x)
for j in range(len(y)):
    sum += int(y[j])
print(sum)
