
def power():
    base = float(input("Enter base number: "))
    pow = float(input("Enter power number: "))
    result = 1 
    for index in range(pow):
        result = result * base
    return result 
    

print(power())

