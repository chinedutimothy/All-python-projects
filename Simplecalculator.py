
#I NEED THE CALCULATOR TO GIVE ME (INT) ANSWERS IN INT
#HOW TO GO BACK TO MAIN MENU INSTEAD OF RESTARTING THE OPERATION
#The root of -64 is wrong when doing it
#very rough work

print ("Enter the keyword for an operation ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Root")

operation = input()

if operation == "1":
    num1 = input("Enter first number")
    num2 = input("Enter second number") 
    x = float(num1)+ float(num2)
    print("The sum is ", x)
elif operation == "2":
    num1 = input("Enter first number")
    num2 = input("Enter second number")
    x = float(num1) - float(num2)
    print("The difference is ", x)
elif operation == "3":
    num1 = input("Enter first number")
    num2 = input("Enter second number")
    x = float(num1) * float(num2)
    print("The product is ",x)
elif operation == "4":
    num1 = input("Enter first number")
    num2 = input("Enter second number")
    x = float(num1) / float(num2)
    print("The result is ", x)
elif operation == "5":
    num1 = input("Enter first number")
    num2 = input("Enter second number")
    x = pow(float(num1), float(num2))
    print("The result is ", x)
elif operation == "6":
    num1 = input("Enter first number")
    num2 = input("Enter second number")
    x = float(num1)**float((float(1)/float(num2)))
    if float(num1)<0:
       (num1) = abs(float(num1))
       x = float(num1)**float(float(1))/float(num2) *float(-1)
       x = float(num1)**float(float(1)/float(num2))

    print("The result is ", x)

else:
    print("invalid entry")


    
