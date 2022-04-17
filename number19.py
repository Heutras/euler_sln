dates = [[1,'Jan',1901,'Tue']]
days = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
small_m = ['Sep','Apr','June','November']
big_m = ['Jan','Mar','May','July','Aug','Oct','Dec']

def Inc(l):
    temp_list = [1]
    m = (months.index(l[1]) + 1) % 12
    temp_list.append(months[m])    
    if l[1] != 'Dec':
        temp_list.append(l[2])
    else:
        temp_list.append(l[2]+1)
    if l[1] in big_m:
        d = (31 - days.index(l[3])) % 7
        x = (days.index(l[3]) + d + 1) % 7
        print("bu d degeri",d,"bu da gün",days[x])
        temp_list.append(days[x])
    elif l[1] in small_m:
        d = (30 - days.index(l[3])) % 7
        x = (days.index(l[3]) + d + 1) % 7
        print("bu d degeri",d,"bu da gün",days[x])
        temp_list.append(days[x])
    else:
        d = (28 - days.index(l[3])) % 7
        x = (days.index(l[3]) + d + 1) % 7
        print("bu d degeri",d,"bu da gün",days[x])
        temp_list.append(days[x])
    return temp_list

n = 0
#dates[-1] != [1,'Feb',1901,'Fri']
while len(dates) <5:
    dates.append(Inc(dates[n]))
    n += 1

for x in dates:
    if(x[0] == 1):
        print(x)
