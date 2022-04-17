def fractionToDecimal(numr, denr):
    res = ""
    mp = {}
    rem = numr % denr
    while ((rem != 0) and (rem not in mp)):
        mp[rem] = len(res)
        rem = rem * 10
        res_part = rem // denr
        res += str(res_part)
        rem = rem % denr
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]
max_val = 0
max_chain = ""
for i in range(1000,0,-1):
    res = fractionToDecimal(1, i)
    if res != "" and len(res) > len(max_chain):
        max_chain = res
        max_val = i

print("answer = ",max_val)