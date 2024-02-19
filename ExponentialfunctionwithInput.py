print("Welcome to Exponential Function")
def power():
    base = int(input("Enter base number: "))
    pow = int(input("Enter power number: "))
    result = 1 
    for index in range(pow):
        result = result * base
    return result 
    

print(power())


