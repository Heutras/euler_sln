single_digits = ["zero", "one", "two", "three",
                 "four", "five", "six", "seven",
                 "eight", "nine"]
two_digits = ["", "ten", "eleven", "twelve",
              "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen",
              "nineteen"]
tens_multiple = ["", "", "twenty", "thirty", "forty",
                 "fifty", "sixty", "seventy", "eighty",
                 "ninety"]
tens_power = ["hundred", "thousand"]

sum_words = 0

def convert_to_words(num):
    temp_str = ""
    l = len(num)

    if (l == 0):
        print("empty string")
        return
 
    if (l > 4):
        print("Length more than 4 is not supported")
        return
    if (l == 1):
        temp_str = temp_str + single_digits[ord(num[0]) - 48]
        return temp_str
    x = 0
    while (x < len(num)):
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                temp_str += single_digits[ord(num[x]) - 48] + tens_power[l - 3]
                if int(num) % 100 != 0:
                    temp_str += "and"
            l -= 1
 
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48)
                temp_str += two_digits[sum]
                return temp_str
 
            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                temp_str += "twenty"
                return temp_str
 
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    temp_str += tens_multiple[i]
                x += 1
                if(ord(num[x]) - 48 != 0):
                    temp_str += single_digits[ord(num[x]) - 48]
        x += 1
    return temp_str
for i in range(1000,0,-1):
    a = str(i)
    b = convert_to_words(a)
    c = len(b)
    sum_words += c
    #print(a, " : ",b," : ",c)
print("result :", sum_words)