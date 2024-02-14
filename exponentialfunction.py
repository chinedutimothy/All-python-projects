def power(base,pow):
    x = 1
    for pig in range(pow):
        x = x * base 
    return x

print(power(2,3))