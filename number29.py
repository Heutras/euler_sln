a = [*range(2, 101, 1)]
b = []
for i in a:
    for j in a:
        val = i**j
        if val not in b:
	        b.append(val)
print(len(b))