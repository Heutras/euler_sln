memo = {}
res_number = []
res_chain = []
def collatz_seq(n):
    if not n in memo:                   # check if already computed
        if n == 1:                      # if not compute it
            memo[n] = 1                 # cache it
        elif n % 2 == 0:
            memo[n] = collatz_seq(n // 2) + 1
        else:
            memo[n] = collatz_seq(3*n + 1) + 1
    return memo[n]                      # and return it
i = 1000000
while i > 1:
    res_number.append(i)
    res_chain.append(collatz_seq(i))
    i -= 1
max_index = res_chain.index(max(res_chain))
max_val = res_number[max_index]
print("answer ->",max_val)