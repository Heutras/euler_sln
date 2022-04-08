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

prime = 11
count = 5
while not (count==10002):
    if (isPrimeNumber(prime)):
        count = count + 1
    prime = prime + 1
print(prime - 1)
