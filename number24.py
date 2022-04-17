all_perm = []
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = [] 
 
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function
data = list('0123456789')
for p in permutation(data):
    all_perm.append(p)
    #print(p)
print("sonuc =",all_perm[999999])