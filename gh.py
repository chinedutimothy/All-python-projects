"""
def xavi(txt):

    first, middle, last = txt.split()

    return first, middle, last

_, _, biggie = xavi("Adiran Calita Perex ")

print(biggie)
"""
"""
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split()

print(x)
"""
"""
def xavi(txt):
     first, middle, last = txt.split() 
     return first, middle, last 

_, _, biggie = xavi("hello, my name is Peter, I am 26 years old")

print(biggie)
"""
"""
client_details = { 'name':['Jax', 'Jim'],
               'occupation':['Lawyer', 'Teacher'],
               'age':[35, 30] }
                       

print('{name[0]} is a {occupation[0]} and'
      ' he is {age[0]} years old.'.format_map(client_details))
        
print('{name[0]} is a {occupation[0]} and'
      ' he is {age[0]} years old.'.format_map(client_details))
"""

#nums = [1,2,3,4]
#[print(nums) for x in nums]

nums =  [1,2,3,4]
[print(nums) for x in nums]
