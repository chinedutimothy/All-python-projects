"""
exponential function allows you to find the power of a number
you can also do this with the (2**3)=8 but we will be using a function and for loop to do so
"""

def power(base_num,power_num): #you call a function with base_num and power_num as the parameters 
    x = 1 #
    for index in range(power_num): #you use the for loop becausen we certainly dont know the power_num and we have to
      x = x * base_num
    return x

print(power(4,6))