import math

def isPrimeNumber( n ):
    n = abs(int(n))
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    r = math.sqrt( n )
    x = 3
    while x <= r:
        if n % x == 0: return False
        x += 2
    return True
sum = 0
for i in range (2, 2000000):
    if (isPrimeNumber(i)):
        sum = sum + i
print(sum)
