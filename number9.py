for a in range(3, 1000):

    for b in range(4, 1000):
        
        c = pow(pow(a, 2)+pow(b, 2), 1/2)

        if a+b+c == 1000:
            print(a * b * c)
            break
        