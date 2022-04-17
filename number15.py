MAX_CHAR = 26
def factorial(n) :
    fact = 1
    for i in range(2, n + 1) :
        fact = fact * i
    return fact
def countDistinctPermutations(st) :
    length = len(st)
    freq = [0] * MAX_CHAR
    
    for i in range(0, length) :
        if (st[i] >= 'a') :
            freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1
   
    fact = 1
    for i in range(0, MAX_CHAR) :
        fact = fact * factorial(freq[i])
   
    return factorial(length) // fact

# If we start from the top left corner and we want to arrive to the bottom right corner we need to calculate our movements, i'll use letter r for going right and d for going down, for a 20x20 grid we need 20 r and 20 d and use a string permutation function. 
st = "rrrrrrrrrrrrrrrrrrrrdddddddddddddddddddd"
print (countDistinctPermutations(st))